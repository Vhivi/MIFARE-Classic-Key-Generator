# MIFARE Classic Key Style Generator 🔑

This project generates a file containing 12-character hexadecimal keys similar to MIFARE Classic keys, ranging from `000000000000` to `FFFFFFFFFFFF`.

## 📖 Description

### ⚙️ Configuration

The [config.ini](config.ini) file defines the generation parameters:

- `output_file`: the name of the output file (default is `keys.txt`)
- `key_length`: the length of each key (12 characters)
- `start`: the starting value in hexadecimal (`0x0`)
- `end`: the ending value in hexadecimal (`0xFFFFFFFFFFFF`)

### 🚀 Key Generation

The [main.py](main.py) script reads the configuration, calculates the total number of keys to generate, and writes each key to the output file.

## 📋 Prerequisites

- Python 3.x installed 🐍
- No specific third-party modules are required (only the standard `configparser` and `os` module are used)

## 🛠️ Usage

1. Configure the parameters in the [config.ini](config.ini) file if necessary.

2. Run the script using the following command in your terminal:

    ```sh
    python main.py
    ```

3. The keys will be generated and saved in the file specified in `output_file` (default is `keys.txt`).

## 📄 Example Output

The output file will contain lines like these:

```txt
000000000000
000000000001
000000000002
...
FFFFFFFFFFFF
```

## 📝 Notes

- The total number of keys generated is calculated based on the difference between the `start` and `end` values defined in the configuration file.
- Ensure that the configuration file (`config.ini`) is in the same directory as `main.py`.

## ⚠️ Warning

**Caution:**

- The key range generated covers all possible values for 12-character hexadecimal keys, which is $16^{12}=(2^4)^{12}=2^{48}=281,474,976,710,656 \text{ keys}$.
- This means the output file will be **extremely** large.
- Each key consists of 12 hexadecimal characters (1 character = 1 byte in ASCII), which is 12 bytes per key + 1 byte for the newline.
- The total file size will therefore be $281,474,976,710,656 \text{ keys} \times 13 \text{ bytes} = 3,659,174,697,238,528 \text{ bytes}$.
- Conversion to practical units:
  - in GB: $\frac{3,659,174,697,238,528}{1024^3} \approx 3,407,872 \text{ GB}$
  - in TB: $\frac{3,407,872}{1024} \approx 3,328 \text{ TB}$
  - in PB: $\frac{3,328}{1024} \approx 3.25 \text{ PB}$
- The final file size will therefore be **3.25 PB** (Petabytes)! 😱
- It is therefore almost **impossible** to generate all the keys at once.

## Acknowledgements

For mathematical notation in Markdown:

- Use `$...$` for inline math, e.g., `$E=mc^2$`.
- This will render as $E=mc^2$.

- For more details, refer to [Cheat Sheet: Adding Math Notation to Markdown](https://www.upyesp.org/posts/makrdown-vscode-math-notation/).

## 📜 License

- For more details, please refer to the [LICENSE](LICENSE) file.

---

Happy key generating! 🎉🔐
