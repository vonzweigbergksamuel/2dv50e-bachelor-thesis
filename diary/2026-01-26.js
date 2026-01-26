// This is an example test for the workshop/tests with junior developers in JavaScript

/* ----- TEST 1 (config file) ----- */
// Typed as a string in TS file
export const numberOfPlanets = "8";

// Typed as a number in TS file
export const numberOfMoons = 27;



/* ----- TEST 1 (in another file, the file where the participant will write the code) ----- */
import { numberOfPlanets, numberOfMoons } from "./2026-01-26";

/**
 * Implement this function to pass the tests
 * 
 * Should return the sum of the planets and moons (the two imported variables) 
 */
function test1() {
    
}

test1();



/* ----- UNIT TESTS: TEST 1 ----- */
import { test1 } from "./2026-01-26";

// The sum should be 35
test("test1", () => {
    expect(test1()).toBe(35);
});

// The result should be a number
test("test1", () => {
    expect(test1()).typeOf("number");
});

// The tests should fail the JS code because a string is added to a number. TS should give a type error hinting about the problem making it easier for the developer to debug and fix the problem.



/* ----- TEST 2 (config file) ----- */
// Should return an object with values varying, ie. it's flaky
export function getFlakyObject() {
    return {
        name: Math.random() > 0.5 ? "John" : "Jane",
        age: Math.random() > 0.5 ? "30" : 25,
        email: Math.random() > 0.5 ? "john@example.com" : "jane@example.com",
        city: Math.random() > 0.5 ? "New York" : "",
    };
}



/* ----- TEST 2 (in another file, the file where the participant will write the code) ----- */
import { getFlakyObject } from "./2026-01-26";

// This is an example type of what the getFlakyObject function returns.
interface FlakyObject {
    name: string;
    age: number | string;
    email: string;
    city: string | undefined | null;
    birthCountry: "Sweden" | "Norway" | "Denmark" | "Finland" | "Other";
}

// This is an example type of what the test2 function should return.
interface Test2Result {
    name: string;
    age: number;
    email: string;
    city: string;
}

/**
 * Implement this function to pass the tests
 * This is a DTO (Data Transfer Object) that will be used to return the data from the getFlakyObject function in a standardized way.
 * 
 * Should return a new object with this structure...
 * Return type will be typed in TS file
 */
function test2(flakyObject) {

}

const flakyObject = getFlakyObject();
test2(flakyObject);



/* ----- UNIT TESTS: TEST 2 ----- */
import { test2 } from "./2026-01-26";

// Create knowingly destructive test data to test the function. The function should handle all possible values from the flakyObject and return the expected data.
test("test2", () => {
    expect(test2(getFlakyObject())).toBe({
        name: "John",
        age: 30,
        email: "john@example.com",
        city: "New York",
    });
});

// The result should be an object
test("test2", () => {
    expect(test2(getFlakyObject())).typeOf("object");
});