# Efficient Reasoning using Self-BackTracking

## Installation Instructions
It's recommended to use Micromamba to setup your project -

```
$Env:MAMBA_ROOT_PREFIX="$HOME\micromambaenv"
micromamba create -y --quiet -f environment.yaml 
micromamba activate efficientreasoning
```

If you update the environment - 

```
micromamba env export -n efficientreasoning > environment2.yml
```

## Usage
To run the application, execute the following command:

```
python src/main.py --configid XXXX
```

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.