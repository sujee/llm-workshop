# Manual Verification

## Prompt

Assume the role of data quality checker.  You will inspect data and make sure it conforms to the following specifications.

- each row is a json data.  Data can be malformed. You need to check for this and handle it gracefully
- if all rows are valid, then only print "Data is OK".  Do not print any analysis.
- if any of the rows are not valid, print out the line number and reason
- if not all rows pass validation then print "Data is NOT OK" at the end.
- each row must have the following attributes: name, age, gender, weight
- if a row is missing any of the above attributes or have extra attributes, point it out and clearly explain the reason
- 'age' attribute should be an integer between 0 and 100
- 'weight' attribute should be a number
- 'gender' attribute can only have one of these three valid values: 'M', 'F', 'N'
- And when 'age' is greater than 20, the 'weight' attribute must be greater than or equl to 100

Here is some sample good data:

```json
{"name": "John", "age": 35, "gender" : "M", "weight": 200.5 }
{"name": "Jane", "age": 40, "gender" : "F", "weight": 150.2}
{"name": "Mike", "age": 18, "gender" : "M", "weight": 120}
{"name": "Sue",  "age": 19, "gender" : "N", "weight": 110}
```

Provide data in JSON format like this.  If the data is ok, here is the desired output

```json
{
    "result": "OK",
    "reason" : ""
}
```

If the data is not ok, provide output like this

```json
{
    "result": "NOT OK",
    "reason" : "provide the reason for failure"
}
```

## If LLM Makes a Mistake?

Give feedback, like

```text
line 3 seems OK.  Reevaluate the data
```

## Data

### Valid data

**Prompt:**

Analyze this data

```json
{"name": "John", "age": 35, "gender" : "M", "weight": 200.5 }
{"name": "Jane", "age": 40, "gender" : "F", "weight": 150.2}
{"name": "Mike", "age": 18, "gender" : "N", "weight": 120}
{"name": "Sue",  "age": 19, "gender" : "F", "weight": 110}
```

**Expected Output:**

```json
{
    "result": "OK",
    "reason": ""
}
```

### Ivalid: Invalid JSON

**Prompt:**

Analyze this data

```json
{"name": "John", "age": 35, "gender" : "M", "weight": 200.5 }
{"name": "Jane", "age": 40, "gender" : "F", "weight": 150.2}
{"name": "Mike", "age": 18, "gender" : "M", "weight": 120}
{"name": "Sue",  "age": 19, "gender" : "F", "weight": x}
```

**Expected Output:**

```json
{
    "result": "NOT OK",
    "reason": "Row 4: 'weight' attribute is not a valid number."
}
```

### Invalid: Missing Attribute

second row is missing "gender" attribute

**Prompt:**

Analyze this data

```json
{"name": "John", "age": 35, "gender" : "M", "weight": 200.5 }
{"name": "Jane", "age": 40, "weight": 150.2}
{"name": "Mike", "age": 18, "gender" : "M", "weight": 120}
{"name": "Sue",  "age": 19, "gender" : "F", "weight": 100}
```

**Expected output:**

```json
{
    "result": "NOT OK",
    "reason": "Row 2: Missing 'gender' attribute."
} 
```

### Invalid: Extra Attribute

3rd row has an extra attribute "height"

**Prompt:**

Analyze this data

```json
{"name": "John", "age": 35, "gender" : "M", "weight": 200.5 }
{"name": "Jane", "age": 40, "gender" : "F", "weight": 150.2}
{"name": "Mike", "age": 18, "gender" : "M", "weight": 120, "height" : 200}
{"name": "Sue",  "age": 19, "gender" : "F", "weight": 100}
```

**Expected output:**

```json
{
    "result": "NOT OK",
    "reason": "Row 3: Contains extra attribute 'height'."
} 
```

### Invalid: Invalid value for 'gender'

We have an invalid gender column here

**Prompt:**

Analyze this data.


```json
{"name": "John", "age": 35, "gender" : "M", "weight": 200.5 }
{"name": "Jane", "age": 40, "gender" : "F", "weight": 150.2}
{"name": "Mike", "age": 18, "gender" : "N", "weight": 120}
{"name": "Sue",  "age": 19, "gender" : "X", "weight": 100}
```

**Expected output:**

```json
{
    "result": "NOT OK",
    "reason": "Row 4: Invalid gender value 'X'. Gender must be one of 'M', 'F', or 'N'."
}
```

### Invalid: invalid age

**Prompt:**

Analyze this data.

```json
{"name": "John", "age": 35, "gender" : "M", "weight": 200.5 }
{"name": "Jane", "age": 40, "gender" : "F", "weight": 150.2}
{"name": "Mike", "age": 18, "gender" : "N", "weight": 120}
{"name": "Sue",  "age": 119, "gender" : "F", "weight": 100}
```

### Invalid: Conditonal Checking of `age` and `weight`

**Prompt:**

Analyze the following data

```json
{"name": "John", "age": 35, "gender" : "M", "weight": 200.5 }
{"name": "Jane", "age": 40, "gender" : "F", "weight": 50.2}
{"name": "Mike", "age": 18, "gender" : "N", "weight": 120}
{"name": "Sue",  "age": 19, "gender" : "F", "weight": 100}
```

**Expected output:**

```json
{
    "result": "NOT OK",
    "reason": "Row 4: Weight should be greater than or equal to 100 when age is greater than 20."
}
```


