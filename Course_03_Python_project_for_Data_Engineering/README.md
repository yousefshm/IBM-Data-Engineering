# ETL Data Processing Pipeline

A lightweight ETL pipeline that processes person data from multiple file formats, converts measurements to metric units, and consolidates the results.

## Sample Data Transformation

Input (example formats):
- CSV/JSON: `{"name":"alex","height":66,"weight":113}`
- XML: `<person><name>alex</name><height>66</height><weight>113</weight></person>`

Output (transformed_data.csv):

name,height,weight
alex,1.67,51.25
ajay,1.82,61.91
...


## Features

- **Multi-format Support**: Processes CSV, JSON, and XML files from `extracted_folder/`
- **Unit Conversion**:
  - Height: Inches → Meters (× 0.0254)
  - Weight: Pounds → Kilograms (× 0.45359237)
- **Data Consolidation**: Merges records from all input files
- **Audit Logging**: Detailed operation timestamps in `log_file.txt`

## File Structure

```
project/
├── etl_code.py            # Main ETL script
├── extracted_folder/      # Input directory (add your files here)
│   ├── *.csv
│   ├── *.json
│   └── *.xml
├── transformed_data.csv   # Output file (generated)
└── log_file.txt          # Operation log (generated)
```

## Usage

1. Place source files in `extracted_folder/` with fields:
   - `name`: String
   - `height`: Numeric (inches)
   - `weight`: Numeric (pounds)

2. Run the pipeline:
   ```bash
   python etl_code.py
   ```

3. Check outputs:
   - `transformed_data.csv`: Metric-converted data
   - `log_file.txt`: Process timestamps

## Sample Outputs

**transformed_data.csv** (first 5 rows):
```csv
,name,height,weight
0,alex,1.67,51.25
1,ajay,1.82,61.91
2,alice,1.76,69.41
3,ravi,1.73,64.56
4,joe,1.72,65.45
```

**log_file.txt**:
```
2025-Feb-09-18:00:54,ETL Job Started
2025-Feb-09-18:00:54,Extract phase Started
2025-Feb-09-18:00:54,Extract phase Ended
... (full process log)
```

## Requirements

- Python 3.x
- pandas (`pip install pandas`)

## Customization

To modify:
1. **Input Formats**: Update `extract_from_*()` functions
2. **Transformations**: Edit the `transform()` function
3. **Output**: Adjust `load_data()` function

## License

MIT License - Free for modification and distribution
```

This version:
1. Has consistent markdown formatting
2. Maintains proper code block indentation
3. Preserves all special characters
4. Uses clean section headers
5. Includes your actual data samples
6. Is ready for immediate use on GitHub

Just copy and paste this entire content into your README.md file.
