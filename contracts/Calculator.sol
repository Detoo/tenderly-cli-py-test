pragma solidity ^0.4.24;

contract Calculator {
    uint c;

    function add(uint a, uint b) public {
        c = a + b;
    }

    function sub(uint a, uint b) public {
        c = a - b;
    }

    function mul(uint a, uint b) public {
        c = a * b;
    }

    function div(uint a, uint b) public {
        c = a / b;
    }

    function getResult() public view returns (uint x) {
        return c;
    }
}
