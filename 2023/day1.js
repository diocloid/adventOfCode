//day1
const year = '2023'
const day = '1'
const env = "test"

const fs = require('fs').promises;
const path = require('path')

async function readFile() {
    try {
        const data = await fs.readFile(path.resolve(__dirname, `day${day}.${env}.txt`), 'UTF-8');
        return data;
    } catch (err) {
        console.log(err);
    }
}

function parseTextToNumber(text) {
    const lowerCaseText = text.toLowerCase(); // Convert to lowercase for case-insensitivity
    switch (lowerCaseText) {
        case 'zero':
            return 0;
        case 'one':
            return 1;
        case 'two':
            return 2;
        case 'three':
            return 3;
        case 'four':
            return 4;
        case 'five':
            return 5;
        case 'six':
            return 6;
        case 'seven':
            return 7;
        case 'eight':
            return 8;
        case 'nine':
            return 9;
        default:
            // If the input doesn't match any known representation, return null or handle accordingly
            return parseInt(text);
    }
}

async function run() {
    const input = await readFile();
    let output = 0
    for (let i = 0; i < input.split('\n').length; i++) {
        line = input.split('\n')[i];
        const pattern = /(?=(\d|one|two|three|four|five|six|seven|eight|nine|zero)).*(\d|one|two|three|four|five|six|seven|eight|nine|zero)/;
        let match = pattern.exec(line);
        
        num = parseInt(`${parseTextToNumber(match[1])}${parseTextToNumber(match[2])}`)
        console.log(`${i+1}: ${match[1]} ${match[2]} = ${num}`)
        output += num
    }
    console.log(output)
}

run();
