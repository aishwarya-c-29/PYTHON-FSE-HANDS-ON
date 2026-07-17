import React, { useEffect, useState } from "react";
import axios from "axios";

function User() {
  const [name, setName] = useState("");

  useEffect(() => {
    axios
      .get("https://jsonplaceholder.typicode.com/users/1")
      .then((res) => setName(res.data.name));
  }, []);

  return <h1>{name}</h1>;
}

export default User;

Output:

 PASS  src/User.test.js
  ✓ renders user name from mocked API (45 ms)

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
Snapshots:   0 total
Time:        1.2 s
