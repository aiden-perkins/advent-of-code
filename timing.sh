total_ms=0
python in.py $1 >/dev/null
for i in {1..100}; do
    output=$({ time python -m 2025."$1"; } 2>&1)
    real_time=$(echo "$output" | grep "real" | sed 's/real[[:space:]]*0m\(.*\)s/\1/')
    ms_value=$(echo "${real_time/./}" | sed 's/^0*//')
    total_ms=$((total_ms + ms_value))
done
echo "${total_ms::-2}.${total_ms: -2}"
