# Using mocks when testing Python

## Background

This quote from Testing Python: Applying Unit Testing, TDD, BDD and Acceptance Testing nicely summarises the role and purpose of test mocks:

> “When you write tests, you may discover that your code interacts with other systems that are assumed to be tested and fully functional, such as call a database or a web service. In these instances, you don’t want to make those calls for real in your test—for a number of reasons. For example, the database or web service may be down and you don’t want that to cause a failing test as part of your build process, which would produce a false positive. Also, those calls may be slow or cost your company money; therefore, if you are running a build every time you check in, your build could get lengthy or cost the company a large bill. This is where mocking and patching come in. They enable you to swap those real calls for dummy responses. This allows you to test that your code behaves as expected under those conditions”

## Example shown here

[Coming soon...]