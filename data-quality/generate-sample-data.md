# Generate Sample Data

## Data Generation Prompt

You are going to generate some sample data according these speficications:

- each row is a json data. 
- each row must have the following attributes: name, age, gender, weight
- 'age' attribute should be an integer higher than 0 and less than 100
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

Generate some sample data.

## Code Generation

Create python code to generate sample data.

See geneareed code : [generate-data.py](generate-data.py)