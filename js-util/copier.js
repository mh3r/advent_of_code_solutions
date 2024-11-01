import * as fs from 'fs';
import * as https from 'https';
import { COOKIE } from './creds.js';

const YEAR = 2019
const baseDir = `${process.cwd()}/advent${YEAR}`;
const sourceDir = `${baseDir}/src`;
const dataDir = `${baseDir}/data`;
const testFile = `${baseDir}/data/test.txt`;


function init() {
    fs.mkdirSync(sourceDir, { recursive: true });
    fs.mkdirSync(dataDir, { recursive: true });
    if (!fs.existsSync(testFile)) {
        fs.writeFile(testFile, 'empty test file', 'utf8', function (err) {
            if (err) return console.log(err);
        });
    }
}

async function copySourceFile(day) {
    const newFileName = `${sourceDir}/day${day}.js`;

    fs.copyFile('js-util/dayx.js', newFileName, (err) => {
        if (err) throw err;
        console.log('File was copied to destination');
    });

    await sleep(1000);
    fs.readFile(newFileName, 'utf8', function (err, data) {
        if (err) {
            return console.log(err);
        }
        const result = data.replace(/dx_input/g, `d${day}_input`).replace(/the_year/g, YEAR);

        fs.writeFile(newFileName, result, 'utf8', function (err) {
            if (err) return console.log(err);
        });
    });


}

function downloadInputFile(day) {
    const file = fs.createWriteStream("./advent" + YEAR + "/data/d" + day + "_input.txt");

    const appurl = "https://adventofcode.com/" + YEAR + "/day/" + day + "/input";
    const url = new URL(appurl);

    const options = {
        host: url.host,
        url: appurl,
        path: url.pathname,
        method: 'GET',
        rejectUnauthorized: false,
        headers: {
            "cookie": COOKIE
        }
    };

    https.get(options, function (response) {
        console.log('STATUS: ' + response.statusCode);
        console.log('HEADERS: ' + JSON.stringify(response.headers, null, 2));
        response.pipe(file);

        // after download completed close filestream
        file.on("finish", () => {
            file.close();
            console.log("Download Completed");
        });
    });

}

function sleep(ms) {
    return new Promise((resolve) => {
        setTimeout(resolve, ms);
    });
}

async function main() {
    init();
    const day = fs.readdirSync(sourceDir).filter(x => x.includes("day")).length + 1;
    await copySourceFile(day);
    downloadInputFile(day);
}



await main();