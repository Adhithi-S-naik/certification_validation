// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Certification {
    struct Certificate {
        string studentName;
        string courseName;
        uint256 date;
    }

    mapping(bytes32 => Certificate) private certificates;

    function addCertificate(bytes32 certHash, string memory studentName, string memory courseName, uint256 date) public {
        certificates[certHash] = Certificate(studentName, courseName, date);
    }

    function getCertificate(bytes32 certHash) public view returns (string memory, string memory, uint256) {
        Certificate memory cert = certificates[certHash];
        return (cert.studentName, cert.courseName, cert.date);
    }
}
