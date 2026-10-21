import * as tools from "../../js-util/tools.js";

async function getResponseFromStash(keyword) {
  if (!STASH_COOKIE) {
    throw new Error(
      "Set STASH_COOKIE to an authenticated Stash session cookie.",
    );
  }

  async function fetchPage(start) {
    const body = {
      query: `project:AU ${keyword}`,
      entities: { code: { start, limit: SEARCH_LIMIT[0] } },
      limits: { primary: SEARCH_LIMIT[0], secondary: SEARCH_LIMIT[1] },
    };

    const response = await fetch(
      "https://msstash.morningstar.com/rest/search/latest/search?",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Cookie: STASH_COOKIE,
        },
        body: JSON.stringify(body),
      },
    );

    if (!response.ok) {
      const details = await response.text();
      throw new Error(
        `Stash search failed: ${response.status} ${response.statusText}${details ? ` - ${details}` : ""}`,
      );
    }

    return response.json();
  }

  function hasMorePages(code) {
    if (
      !code ||
      code.isLastPage === true ||
      !Number.isFinite(code.start) ||
      !Number.isFinite(code.nextStart) ||
      code.nextStart <= code.start
    ) {
      return false;
    }

    return !(
      Number.isFinite(code.count) &&
      code.count >= code.start &&
      code.count <= code.nextStart
    );
  }

  function mergePage(target, page) {
    target.code.values.push(...page.code.values);
    for (const key of ["isLastPage", "count", "start", "nextStart"]) {
      target.code[key] = page.code[key];
    }
    return target;
  }

  const result = await fetchPage(0);

  result.code.keyword = keyword;

  if (!hasMorePages(result.code)) {
    return result;
  }

  if (!FETCH_ALL) {
    console.log(
      `WARNING: More results are available for '${keyword}' - set FETCH_ALL to true to fetch all pages. (${result.code.count} total, ${result.code.start} shown)`,
    );
    return result;
  }

  while (hasMorePages(result.code)) {
    try {
      const nextStart = result.code.nextStart;
      const page = await fetchPage(nextStart);
      if (!page.code || page.code.start !== nextStart) {
        throw new Error("Stash search pagination did not advance.");
      }
      mergePage(result, page);
    } catch {
      console.log(`ERROR - Unable to display more results for '${keyword}'`);
      return result;
    }
  }

  return result;
}

function parseMultiLineToUniqueEntries(raw) {
  return Array.from(
    new Set(
      raw
        .split("\n")
        .map((line) => line.trim())
        .filter((line) => line.length > 0),
    ),
  );
}

function analyseResponses(responses) {
  if (!POV_PROJECTS) {
    console.log("Only Project perspective is implemented!");
  }

  const resultMetrix = new Map();

  for (const response of responses) {
    if (response.code && response.code.values.length > 0) {
      // console.log(`Processing '${response.code.keyword}' ...`);

      for (const hit of response.code.values) {
        const projectName = hit.repository.name;
        if (!resultMetrix.has(projectName)) {
          resultMetrix.set(projectName, []);
        }
        if (!resultMetrix.get(projectName).includes(response.code.keyword)) {
          resultMetrix.get(projectName).push(response.code.keyword);
        }
      }
    }
  }

  return resultMetrix;
}

function printResultMetrix(resultMetrix) {
  if (resultMetrix.size === 0) {
    console.log("No results found.");
    return;
  }

  if (EXCLUDE_INPUT && EXCLUDE_INPUT.length > 0) {
    console.log(`Excluded keywords: ${EXCLUDE_INPUT.join(", ")}`);
    console.log("");
  }
  console.log("");
  console.log("Result Metrix:");
  console.log("");

  for (const [project, keywords] of resultMetrix.entries()) {
    console.log(`*${project}:*`);
    console.log(`Keywords: ${keywords.join(", ")}`);
    console.log("");
  }
}

async function main() {
  const keywords = INPUT.filter((keyword) => !EXCLUDE_INPUT.includes(keyword));

  console.log("Keywords to search:");
  console.log(keywords);
  const responses = await Promise.all(
    keywords.map((keyword) => getResponseFromStash(keyword)),
  );

  const resultMetrix = analyseResponses(responses);
  printResultMetrix(resultMetrix);
}

const SEARCH_LIMIT = [50, 30];

const FETCH_ALL = false;

const POV_PROJECTS = true;

const STASH_COOKIE =
  "SPC-SELECTED-CATEGORY-AU=all; SPC-SELECTED-CATEGORY=7; apt.uid=AP-YFGMCGUNNIFB-2-1787718189443-98518198.0.2.e4e1a566-10eb-454c-b1f2-fc0d1b8d1d8f; msession=1c6eb21c-85d6-4418-adde-58d43584875a.111168b9fb6b9544e15514e1a35f03c9954c9a8d56f4f8db71018d98e3fa6549; _parsely_visitor={%22id%22:%22pid=d53e3d72-28a0-4f18-a515-d267e251db5a%22%2C%22session_count%22:1%2C%22last_session_ts%22:1790744160135}; AwinChannelCookie=direct; _gcl_au=1.1.1478466893.1790744160; _rdt_uuid=1790744160476.daa5fc48-7976-47db-96cc-f18f3d413afb; _uetvid=c791a220ef7311f09e6c7150b0bf9999; mprtcl-v4_55148BDC={'gs':{'ie':1|'dt':'us2-9ff2735df8dd704a81c196f890607ec8'|'cgid':'3dab84cd-ff6a-4647-fae8-b70fa136c3c9'|'das':'03b5d5f7-c60a-4a55-b7d0-2b7fe04fe88a'}|'l':0}; _clck=2gkhy7%5E2%5Eg9w%5E0%5E2464; ELOQUA=GUID=F7DC779F5718442A85D69A2008F445F1; mid=9282438950423966756; _ga_G8C0R44VCK=GS2.1.s1790744160$o1$g0$t1790744162$j58$l0$h0; _gid=GA1.2.1273839838.1792360208; _ga_SW6G2BFREG=GS2.1.s1792366389$o1$g1$t1792366574$j60$l0$h0; _ga_LMTVSGTMT2=GS2.1.s1792366390$o1$g1$t1792366574$j60$l0$h0; _ga_DLZP83KFTR=GS2.1.s1792366390$o1$g1$t1792366574$j60$l0$h0; ms-sso2=ODViZGU5NjktNGU3My00YjIyLTg3OTMtOTQzMzg0OGVjYTQ3; _ga=GA1.1.1374526563.1786593447; _ga_2ZL1MZMF4N=GS2.1.s1792536102$o170$g1$t1792536944$j60$l0$h0; _atl_bitbucket_remember_me=NzZmMzE2MDljMzllYjJhMTVhMDMwMzE1MGFjMjNhZDVlMDE2ZDIzNDoxNTQ0OTdiNTY1YjJkMmE4NDU2MGJjYWNkNGFjM2ExNzE3ZjBlNzA1; BITBUCKETSESSIONID=0D5171CAE3B0389E5D21F4EF0FA6CAE6";

const INPUT = parseMultiLineToUniqueEntries(`

CMSStarRatingsIntraday
CMSStarRatingsEndDay
CMSRecommendationChanges 
spCMS_GenExceptionReport
vCMSRecommendationChanges
vCMS_LatestRecommendationChanges
vCMS_LatestRecommendationChanges_NoPriceChange
vCMSRecommendationChangesIncUC
vCMS_LatestRecommendationChangesIncUC
CustomFeed_Sparky
spGet_SparkyYMW
vCMSRecommendationChanges
spCMS_LatestYmwPDFVersion
spCMS_RecommendationChange
spCMS_SEL_AfternoonNoteRecChanges
spCMS_StarRatingEOD
spCMS_StarRatingRR
spCMS_StockRec
spCMS_YesterdayRecommendationChanges
spCMS_YmwPrintVersion
spGet_AllUniverseResearchEvents
spGet_StockLatestUpdates
spGet_StockResearchAdvanceForClientSecuritiesGet_cms
spGet_StockResearchForClientSecuritiesGet_cms
view_ArcResearchRec
RecommendationHistory
EventHeader
ResearchTriggers 
view_srResearchDate
AfternoonNoteRecChanges
MarketUpdateResearch 
RecommendationChanges
RecommendationChangesNewsletters
RecommendationHistoryASXCode
vCMS_AfternoonNoteRecommendationChanges_MCA
vCMS_AfternoonNoteResearchReleased_MCA
vCMS_LatestRecommendationChanges
vCMSRecommendationChanges
spCMS_SEL_AfternoonNoteRecChanges
spSEL_HistoricalFinancials
spSEL_AfternoonNoteRecChanges
ResearchlinkFinancials
spGet_AVMMarketUpdates

`);

const EXCLUDE_INPUT = parseMultiLineToUniqueEntries(`
EventHeaderasdf

`);

await main();
