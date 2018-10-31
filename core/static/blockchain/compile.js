const path = require('path');
const fs =  require('fs');
const solc = require('solc');

const contractPath = path.resolve('/mnt/d','blockchian','smartSponsor.sol');
const source =fs.readFileSync(contractPath,'UTF-8');

//module.exports = solc.compile(source,1).contracts[':SmartSponsor']
//console.log(solc.compile(source,1))
console.log(source)
