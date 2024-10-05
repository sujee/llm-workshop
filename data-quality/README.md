# Data Quality Check with LLM

We will use an LLM to verify data.  And generate code to verify data.

Our data is JSON

```json
{"name": "John", "age": 35, "gender" : "M", "weight": 200.5 }
{"name": "Jane", "age": 40, "gender" : "F", "weight": 150.2}
{"name": "Mike", "age": 18, "gender" : "M", "weight": 120}
{"name": "Sue",  "age": 19, "gender" : "N", "weight": 110}
```


## Step-1: Manual Verification

See here for prompts and sample data.

[manual-verification.md](./manual-verification.md)

## Step-2: Generate Sample Data

[generate sample data](./generate-sample-data.md)

## Step-3: Code to verify data

[code-gen.md](./codegen.md)

---

```text
Can you generate python code to accomplish this?  Make sure the code can handle malformed data as well
```