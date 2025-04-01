### Digital Audio
- Digital audio is a representation of sound in a digital format.
- In digital audio, the sound wave of the audio signal is encoded as numerical samples in continuous sequence.
- It is stored in a file format that can be played back by a computer or other digital audio player.


### sample
- A sample is a value of the audio signal at a particular point in time and space.
- The sample rate is the number of samples of audio carried per second, measured in Hz or kHz.
- The sample size is the number of bits of information in each sample, and it determines the dynamic range of the audio signal.
- The sample format is the way in which the audio signal is represented in the digital domain, such as PCM or MP3.

### Sample Rate
- The sample rate is the number of samples of audio carried per second, measured in Hz or kHz.
- The sample rate is determined by the Nyquist theorem, which states that the sample rate must be at least twice the highest frequency of the audio signal in order to accurately reproduce the sound.
- Common sample rates for digital audio are 44.1 kHz (CD quality), 48 kHz (DVD quality), and 96 kHz (high-definition audio).

### Sample Size
- The sample size is the number of bits of information in each sample, and it determines the dynamic range of the audio signal.
- The sample size is typically 16 bits for CD-quality audio, which provides a dynamic range of 96 dB.
- Higher sample sizes, such as 24 bits, can provide a greater dynamic range and better signal-to-noise ratio.
- In modern computer audio, 32-bit floating-point samples are commonly used for processing and mixing audio.
    - This allows for a virtually unlimited dynamic range and reduces the risk of clipping or distortion.
    - Accomodate for the increased dynamic range of modern audio equipment and the demands of digital audio processing.

### Sample Format
- The sample format is the way in which the audio signal is represented in the digital domain.
- The most common sample format is PCM (Pulse Code Modulation), which represents the audio signal as a series of amplitude values.
- Other sample formats, such as MP3, use compression algorithms to reduce the file size of the audio signal.
- Lossless compression formats, such as FLAC, preserve the original audio signal without any loss of quality.
- Lossy compression formats, such as MP3, reduce the file size by discarding some of the audio data, which can result in a loss of quality.

### Digital Audio Workstation (DAW)
- A digital audio workstation (DAW) is a software application or electronic device used for recording, editing, and producing audio files.
- DAWs are commonly used in music production, sound design, and audio engineering.
- Popular DAWs include Pro Tools, Logic Pro, Ableton Live, and FL Studio.
- DAWs provide a range of features, such as multitrack recording, MIDI sequencing, audio editing, and virtual instruments.
- DAWs allow users to create, edit, and mix audio tracks, as well as apply effects and process audio signals.

### MIDI
- MIDI (Musical Instrument Digital Interface) is a technical standard that describes a protocol, digital interface, 
and connectors that allow a wide variety of electronic musical instruments, computers, and other related devices to connect and communicate with one another.
- A single MIDI link can carry up to sixteen channels of information, each of which can be routed to a separate device.
- MIDI carries event messages that specify notation, pitch, velocity, vibrato, panning, and clock signals.
- MIDI technology allows for the synchronization of music sequencers, lighting systems, and other devices to control sound generation and effects processing.

### Audio File Formats
- Audio file formats are used to store digital audio data on a computer or other digital device.
- Common audio file formats include WAV, AIFF, MP3, AAC, and FLAC.
- WAV (Waveform Audio File Format) and AIFF (Audio Interchange File Format) are uncompressed audio file formats that provide high-quality audio.
- MP3 (MPEG-1 Audio Layer 3) and AAC (Advanced Audio Coding) are lossy compression formats that reduce the file size of audio data.
- FLAC (Free Lossless Audio Codec) is a lossless compression format that preserves the original audio data without any loss of quality.
- Each audio file format has its own advantages and disadvantages in terms of file size, audio quality, and compatibility with different devices and software.

### Audio Interfaces
- An audio interface is a device that connects audio equipment to a computer or other digital device.
- Audio interfaces provide analog-to-digital and digital-to-analog conversion, allowing audio signals to be recorded and played back on a computer.
- Audio interfaces typically include microphone preamps, line inputs, instrument inputs, and headphone outputs.
- Audio interfaces are used in music production, sound recording, and audio engineering to capture and process audio signals.
- Popular audio interface manufacturers include Focusrite, Universal Audio, PreSonus, and Apogee.

### Digital Signal Processing (DSP)
- Digital signal processing (DSP) is the process of analyzing and modifying digital signals to improve their quality or extract useful information.
- DSP is used in audio processing, speech recognition, image processing, and telecommunications.
- In audio processing, DSP algorithms are used to filter, equalize, compress, and enhance audio signals.
- DSP can be implemented in software, hardware, or a combination of both.
- DSP algorithms are used in digital audio workstations, audio plugins, and audio effects processors to manipulate audio signals in real time.

### Audio Effects
- Audio effects are tools used to modify the sound of audio signals in various ways.
- Common audio effects include equalization, compression, reverb, delay, chorus, and distortion.
- Audio effects can be applied to individual tracks, groups of tracks, or the master output of a mix.
- Audio effects are used in music production, sound design, and audio engineering to enhance the quality and creativity of audio recordings.
- Audio effects can be implemented as hardware units, software plugins, or built-in features of digital audio workstations.


### Common Math Operations in Digital Audio & Sampling & Frequency
- Frequency:
    - The frequency of a sound wave is the number of cycles of the wave that occur in one second.
    - Formula: f = 1 / T    where, (f = frequency, T = period)
    - The unit of frequency is Hertz (Hz).
    - The human ear can hear frequencies in the range of 20 Hz to 20 kHz.
- Sampling:
    - Sampling is the process of converting a continuous signal into a discrete signal by taking samples at regular intervals.
    - Formula: fs = 1 / Ts    where, (fs = sampling frequency, Ts = sampling period)
- Sampling Rate: 
    - The number of samples taken per second is called the sampling rate.
    - Relation between frequency and sampling rate: fs = 2 * fmax    where, (fs = sampling rate, fmax = maximum frequency)

- Nyquist Theorem:
    - The Nyquist theorem states that in order to accurately reproduce a signal, the sampling rate must be at least twice the highest frequency of the signal.
    - The Nyquist frequency is half the sampling rate.
    - The Nyquist frequency is the highest frequency that can be accurately represented in a digital signal.
    - The Nyquist frequency is also known as the folding frequency.

- Aliasing:
    - Aliasing is a distortion that occurs when a signal is sampled at a rate lower than the Nyquist rate.
    - Aliasing causes high-frequency signals to be incorrectly represented as low-frequency signals.
    - Aliasing can be prevented by using a sampling rate that is at least twice the highest frequency of the signal.

- Quantization:
    - Quantization is the process of converting a continuous signal into a discrete signal by rounding the sample values to the nearest quantization level.
    - The number of quantization levels determines the resolution of the digital signal.
    - The quantization error is the difference between the original analog signal and the quantized digital signal.
    - The quantization error can introduce noise and distortion into the digital signal.

- Bit Depth:
    - Bit depth is the number of bits used to represent each sample in a digital signal.
    - Bit depth determines the dynamic range of the digital signal.
    - Common bit depths are 16-bit (CD quality), 24-bit (high-definition audio), and 32-bit floating-point (professional audio).
    - Higher bit depths provide a greater dynamic range and reduce quantization noise.

- Dithering:
    - Dithering is a technique used to reduce quantization noise in digital audio signals.
    - Dithering adds a small amount of noise to the signal to mask the quantization error.
    - Dithering is commonly used when reducing the bit depth of a signal, such as when converting from 24-bit to 16-bit audio.
    - Dithering can improve the perceived audio quality of low-bit-depth signals.

- Fast Fourier Transform (FFT):
    - The Fast Fourier Transform (FFT) is an algorithm used to compute the frequency spectrum of a signal.
    - The FFT converts a time-domain signal into a frequency-domain signal.
    - The FFT is used in audio processing to analyze and manipulate the frequency content of audio signals.
    - The FFT is commonly used in audio effects, such as equalization, filtering, and spectral analysis.


### Audio Processing Techniques

- Convolution:
    - Convolution is a mathematical operation that combines two signals to produce a third signal.
    - Convolution is used in audio processing to apply effects, such as reverb and delay.
    - Convolution reverb is a technique that uses convolution to simulate the reverberation of a physical space.
    - Convolution is computationally intensive and is often implemented using the Fast Fourier Transform (FFT) algorithm.

- Digital Filters:
    - Digital filters are algorithms used to process digital signals by removing or enhancing specific frequency components.
    - Digital filters are used in audio processing to equalize, filter, and shape the frequency response of audio signals.
    - Common types of digital filters include low-pass, high-pass, band-pass, and notch filters.
    - Digital filters can be implemented using finite impulse response (FIR) or infinite impulse response (IIR) algorithms.

- Audio Synthesis:
    - Audio synthesis is the process of generating sound waves using electronic or digital devices.
    - Audio synthesis can be achieved using oscillators, samplers, and physical modeling techniques.
    - Audio synthesis is used in music production, sound design, and audio engineering to create new and unique sounds.
    - Common audio synthesis techniques include subtractive synthesis, additive synthesis, and frequency modulation synthesis.

- Audio Compression:
    - Audio compression is the process of reducing the file size of audio data by removing redundant or unnecessary information.
    - Lossless compression algorithms preserve the original audio data without any loss of quality.
    - Lossy compression algorithms reduce the file size by discarding some of the audio data, which can result in a loss of quality.
    - Common audio compression formats include MP3, AAC, and FLAC.
    - Audio compression is used to store and transmit audio data more efficiently.

- Audio Streaming:
    - Audio streaming is the process of transmitting audio data over a network in real time.
    - Audio streaming services deliver audio content to users over the internet.
    - Audio streaming can be live or on-demand, and can be delivered in various formats, such as MP3, AAC, and FLAC.
    - Audio streaming services include Spotify, Apple Music, and Tidal.
    - Audio streaming has revolutionized the music industry by providing instant access to a vast library of music.
