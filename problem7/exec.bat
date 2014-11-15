python samples_generator.py --bound="upper" --samples-number=100 --threshold=5.0 --ini=0.0  --end=10.0 --output-file="upper_samples.json"
python samples_generator.py --bound="lower" --samples-number=100 --threshold=3.0 --ini=0.0  --end=10.0 --output-file="lower_samples.json"

python main.py --lower_bound_tranning_data_file="lower_samples.json" --upper_bound_tranning_data_file="upper_samples.json"