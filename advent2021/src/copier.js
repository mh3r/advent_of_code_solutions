import * as fs from 'fs';
import * as tools from '../../tools.js';
import * as https from 'https';
import { COOKIE } from './creds.js';

async function main() {

    const baseDir = "D:/aoc/advent2021/src/";
    const files = fs.readdirSync(baseDir).filter(x => x.includes("day"));

    const day = files.length;
    const newFileName = `${baseDir}day${day}.js`;

    fs.copyFile(baseDir + 'dayx.js', newFileName, (err) => {
        if (err) throw err;
        console.log('File was copied to destination');
    });

    await sleep(1000);
    fs.readFile(newFileName, 'utf8', function (err, data) {
        if (err) {
            return console.log(err);
        }
        const result = data.replace(/dx_input/g, `d${day}_input`);

        fs.writeFile(newFileName, result, 'utf8', function (err) {
            if (err) return console.log(err);
        });
    });


    downloadInputFile(day);

    tools.cprint(newFileName)
}




function downloadInputFile(day) {
    const file = fs.createWriteStream("D:/aoc/advent2021/data/d" + day + "_input.txt");

    const appurl = "https://adventofcode.com/2021/day/" + day + "/input";
    const url = new URL(appurl);

    const options = {
        host: url.host,
        url: appurl,
        path: url.pathname,
        method: 'GET',
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

await main();