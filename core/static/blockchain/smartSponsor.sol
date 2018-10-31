/** 
    @title Shape calculator.
*/
pragma solidity ^0.4.0;

contract smartSponsor {
  address public owner;
  address public benefactor;
  bool public refunded;
  bool public complete;
  bool private PayByCash;
  uint public numPledges;
  uint public startDate;
  uint public endDate;
  uint public targetAmount;
  uint private AmountForOwner;
  uint private AmountForBenefactor;

  struct Pledge {
    uint amount;
    address eth_address;
    bytes32 message;
  }
  
  mapping(uint => Pledge) public pledges;

  // constructor
  function smartSponsor(address _benefactor , uint _targetAmount , bool payType)payable {
    owner = msg.sender;
    targetAmount = _targetAmount;
    numPledges = 0;
    PayByCash = payType;
    refunded = false;
    complete = false;
    benefactor = _benefactor;
    startDate = now;
    //endDate = _enddate;
  }

  // add a new pledge
  // every can invest , so every can actice this function
  function pledge(bytes32 _message) payable {
    if (msg.value == 0 || complete || refunded) throw;
    pledges[numPledges] = Pledge(msg.value, msg.sender, _message);
    numPledges++;
  }

  function getPot() constant returns (uint) {
    return this.balance;
  }
  
  function getEndDate() constant returns (uint) {
    return endDate;
  }

  // refund the backers
  function refund() {
    if (msg.sender != owner || complete || refunded || this.balance>targetAmount) throw;
    for (uint i = 0; i < numPledges; ++i) {
      pledges[i].eth_address.send( (pledges[i].amount*96)/100 ) ;   // 4% of tax will be charged from each backers' pledge value , if funds is fail
      owner.send((pledges[i].amount*4)/100);
      
    }
    refunded = true;
    complete = true;
  }

  // send funds to the contract benefactor
  function drawdown() {
    if (msg.sender != owner || complete || refunded || this.balance<targetAmount) throw;
    // 7% of tax will be charged from contract balance to us  , if funds is successful
    if(PayByCash !=true){
        AmountForOwner = (this.balance*7)/100;
        AmountForBenefactor = (this.balance*93)/100;
        owner.send(AmountForOwner);
        benefactor.send(AmountForBenefactor);
    }
    else{
        owner.send(this.balance);
    }
    
    
    complete = true;
  }
}