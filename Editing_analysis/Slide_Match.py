import numpy as np

def get_unit_count(sequence):
    return len(sequence) // 4

def sliding_window(sequence, window_width):
    # Generate a sliding window, with one step length of 4 bases/char
    step_size = 4
    for i in range(0, len(sequence) - window_width * 4 + 1, step_size):
        yield i, sequence[i:i + window_width * 4]

def match_count(sample_subseq, sample_index, pool_sequences, window_width, matrix, sample_sequence_num):
    count = 0
    for pool_seq in pool_sequences:
        for index, subseq in sliding_window(pool_seq, window_width):
            if sample_subseq == subseq:
                count += 1
                matrix[sample_sequence_num, sample_index // 4: sample_index // 4 + window_width] = window_width
    return count

def main():
    with open("pool.txt", "r") as pool_file:
        pool_sequences = [line.strip() for line in pool_file]
    pool_unit_count = get_unit_count(pool_sequences[0])

    with open("sample.txt", "r") as sample_file:
        sample_sequences = [line.strip() for line in sample_file]
    sample_unit_count = get_unit_count(sample_sequences[0])

    # Create matrix for intuitive visualization
    matrix = np.zeros((len(sample_sequences), sample_unit_count), dtype=int)

    max_window_width = min(pool_unit_count, sample_unit_count)
    results = []

    for i, sample_seq in enumerate(sample_sequences):
        scores = []
        for window_width in range(1, max_window_width + 1):
            total_count = 0
            for sample_index, subseq in sliding_window(sample_seq, window_width):
                total_count += match_count(subseq, sample_index, pool_sequences, window_width, matrix, i)
            scores.append(str(total_count))
        results.append(f"Sequence{i + 1} {sample_unit_count} {pool_unit_count} {' '.join(scores)}")

    # Output ranking result
    with open("output.txt", "w") as output_file:
        for result in results:
            output_file.write(result + "\n")

    # Output matrix for visualization 
    with open("matrix_output.txt", "w") as matrix_file:
        for row in matrix:
            matrix_file.write(' '.join(map(str, row)) + "\n")

if __name__ == "__main__":
    main()
