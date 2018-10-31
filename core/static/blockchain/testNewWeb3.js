

var Web3 = require('web3');
//var url = 'https://ropsten.infura.io/v3/866424fc5e1643f0837915f33cdb8565';
var url = 'http://127.0.0.1:7545'

//console.log("url = " + url);
var web3 = new Web3(url)
//var address = '0xe829549a68c484af37e0a940d1bbcebfb4a59299';//ropsten account
var account1 = '0xCdC04e82039B4dE2be2E2803cc1CE00A7900854C'
var account2= '0x508256Fb95abECcdCeD0F5Fc0A7b581Ec8E8fB5C'
//console.log("address = " + address);


web3.eth.getBalance(account1,(err,result) =>{ 
	console.log('account  balance:', web3.utils.fromWei(result,'ether'))
});


//console.log(Web3);