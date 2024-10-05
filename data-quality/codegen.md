# Code Gen

## Code to generate data

## Code to verify data

**Prompt**

Generate python code to validate data according to to these specifications


- each row is a json data.  Data can be malformed. You need to check for this and handle it gracefully
- if any of the rows are not valid, print out the line number, the data and the reason
- each row must have the following attributes: name, age, gender, weight
- if a row is missing any of the above attributes or have extra attributes, point it out and clearly explain the reason
- 'age' attribute should be an integer higher than 0 and less than 100
- 'weight' attribute should be a number
- 'gender' attribute can only have one of these three valid values: 'M', 'F', 'N'
- And when 'age' is greater than 20, the 'weight' attribute must be greater than or equl to 100

Here is some sample of valid data:

```json
{"name": "John", "age": 35, "gender" : "M", "weight": 200.5 }
{"name": "Jane", "age": 40, "gender" : "F", "weight": 150.2}
{"name": "Mike", "age": 18, "gender" : "M", "weight": 120}
{"name": "Sue",  "age": 19, "gender" : "N", "weight": 110}
```

The python function will work as follows:

If all rows pass validation return the output in json format like this

```json
{
    "result" = "OK",
    "num_invalid_rows" = 0,
}
```

If not all rows pass validation return output in json format like this:

```json
{
    "result" = "NOT OK",
    "num_invalid_rows" = 1,
}
```