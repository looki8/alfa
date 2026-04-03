# alfa

A simple memory information utility similar to the Unix `free` command.

## Description

This tool displays information about system memory usage, including:
- Total, used, and free memory
- Buffer and cache memory
- Available memory
- Swap usage

## Usage

Run the script directly:

```bash
python3 free.py
```

Or make it executable and run:

```bash
chmod +x free.py
./free.py
```

To see help information:

```bash
python3 free.py --help
```

## Output

The tool displays memory information in a formatted table:

```
               total         used         free       shared   buff/cache    available
          Mem:  [memory values in KB]
         Swap:  [swap values in KB]
```

## Requirements

- Python 3.x
- Linux system with `/proc/meminfo` (for real data) or any system (will use mock data)

## License

Free and open source.
