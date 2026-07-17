import React from "react";
import { render, screen, waitFor } from "@testing-library/react";
import "@testing-library/jest-dom";
import axios from "axios";
import User from "./User";

// Mock axios
jest.mock("axios");

test("renders user name from mocked API", async () => {
  // Fake API response
  axios.get.mockResolvedValue({
    data: {
      name: "Alice"
    }
  });

  render(<User />);

  // Wait until the API response is rendered
  await waitFor(() => {
    expect(screen.getByText("Alice")).toBeInTheDocument();
  });

  // Verify API was called
  expect(axios.get).toHaveBeenCalledTimes(1);
  expect(axios.get).toHaveBeenCalledWith(
    "https://jsonplaceholder.typicode.com/users/1"
  );
});
