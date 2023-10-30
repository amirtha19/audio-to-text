import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

def record_audio():
    # Get recording duration from the user
    duration = float(input("Enter recording duration (in seconds): "))

    # Get the desired output file name from the user
    output_file = input("Enter the output file name (e.g., 'audio.wav'): ")

    # Sampling frequency
    freq = 44100
    print("Recording audio started...")

    # Start recorder with the given values
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

    # Record audio for the given number of seconds
    sd.wait()

    # Convert the NumPy array to an audio file with the given sampling frequency
    write(output_file, freq, recording)

    print(f"Audio recorded and saved as '{output_file}'")

    return output_file
