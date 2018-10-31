var Tx = require('ethereumjs-tx')
const Web3 = require('web3')
const BigNumber = require('big-number')
const web3 = new Web3('https://ropsten.infura.io/v3/866424fc5e1643f0837915f33cdb8565')
//ropsten test network

//public key of wallet address
const account1 = '0xad0ae37863ba0ce04fe52daccbb76adeb26f1a2c'
const account2 = '0x6dbe1254367aed4bbc61936410d0370b1559f1ef'
const account3 = '0xe829549a68c484af37e0a940d1bbcebfb4a59299'
const account4 = '0xf827273cf48f1f4bd0c7f5865ea1f3516baa9d77'
const account5 = '0x0fE3002DE20D5E1e6f562B22938d27f9d498A39F'

/*
//private key of wallet address
export PRIVATE_KEY_1='0xF1C267B0ADF1F4E66B7C862A2008F17F06B7649D0CD8938E76985093D86CF4C7'
export PRIVATE_KEY_2='0xFF8A2B0A5B5C2CC127BD3845AD318590EC2C576085F895CAA54CD812BC0BB9A1'
export PRIVATE_KEY_3='0xA81A3BCA3CE9E8DEBDA183CC7FDF66326B7249EC5F0D2CD7EC65FBFCE8E4C65F'
export PRIVATE_KEY_4='0x36689a3f38d86bc44947f5dac466413e74daceb40982fcc71dd0482edc873750'
export PRIVATE_KEY_5='0xfb32d805a348ea351a71b44b58fc57687b06bdf7c1f7ba8edffd32d0ac34c0cc'
*/

//convert to binary data
const privateKey1 = Buffer.from('0xF1C267B0ADF1F4E66B7C862A2008F17F06B7649D0CD8938E76985093D86CF4C7')
const privateKey2 = Buffer.from('0xFF8A2B0A5B5C2CC127BD3845AD318590EC2C576085F895CAA54CD812BC0BB9A1')
const privateKey3 = Buffer.from('0xA81A3BCA3CE9E8DEBDA183CC7FDF66326B7249EC5F0D2CD7EC65FBFCE8E4C65F')
const privateKey4 = Buffer.from('0x36689a3f38d86bc44947f5dac466413e74daceb40982fcc71dd0482edc873750')
const privateKey5 = Buffer.from('0xfb32d805a348ea351a71b44b58fc57687b06bdf7c1f7ba8edffd32d0ac34c0cc')


web3.eth.getBalance(account1,(err,bal)=>{
	console.log('account 1 balance:', web3.utils.fromWei(bal,'ether'))
})

web3.eth.getBalance(account2,(err,bal)=>{
	console.log('account 2 balance:', web3.utils.fromWei(bal,'ether'))
})

web3.eth.getBalance(account3,(err,bal)=>{
	console.log('account 3 balance:', web3.utils.fromWei(bal,'ether'))
})

web3.eth.getBalance(account4,(err,bal)=>{
	console.log('account 4 balance:', web3.utils.fromWei(bal,'ether'))
})


web3.eth.getBalance(account5,(err,bal)=>{
	console.log('account 5 balance:', web3.utils.fromWei(bal,'ether'))
})

