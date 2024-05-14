
# RokuRemapper

RokuRemapper is a tool designed to remap app launch buttons on your Roku device. This tool listens for specific app launches and redirects them to a different app based on your configuration.

## Features

- Detects when a specific app is launched on your Roku device.
- Automatically redirects the launch to another app.
- Simple configuration through a `remap.config` file.

## Requirements

- Python 3.x
- `requests` library
- Roku device on the same network

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/rokuremapper.git
    cd rokuremapper
    ```

2. Install the required Python packages:
    ```bash
    pip install requests
    ```

3. Make sure your Roku device is connected to the same network as your computer.

## Configuration

The first time you run the script, it will prompt you for the necessary configuration details:

- **App Name to Remap From:** The exact name of the app you want to detect.
- **IP Address:** The IP address of your Roku device (found in Roku settings).
- **App ID to Remap To:** The app ID of the target app (found at `http://your_roku_ip:8060/query/apps`).

These details will be saved in a `remap.config` file for future use.

## Usage

To start the RokuRemapper tool:

```bash
python rokuremapper.py
```

The tool will start listening for app launches and will remap the specified app to your target app.

## Example

Here’s an example of the configuration process:

```
Enter your app name to remap from. MUST BE EXACT: Netflix
Enter your IP address. You can get this from the Roku settings: 192.168.1.100
Enter your app id to remap to. You can get this from http://your_roku_ip:8060/query/apps: 12
```

The `remap.config` file will be created with the following content:

```
[1]
appname = Netflix
ipaddress = 192.168.1.100
appidto = 12
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Disclaimer

Use this tool at your own risk. The author is not responsible for any damage caused by improper use of this tool.

```

Feel free to customize it further to fit your project's needs.
