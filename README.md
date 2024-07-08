# YouTube Daily Summarizer

## Overview

YouTube Daily Summarizer is a tool designed to provide concise summaries of videos from specified YouTube channels. Additionally, it identifies and highlights key overlaps across multiple channels, helping you stay updated with the latest information in a time-efficient manner.

## Features

- **Daily Video Summaries**: Summarizes daily videos from selected YouTube channels.
- **Text Conversion**: Converts the full content of videos into text, allowing for quick reading and understanding of video content.
- **Key Overlaps Analysis**: Analyzes daily video content from multiple channels to identify key overlaps and insights.  
  For example, if multiple investment channels discuss the same information, this consensus indicates important and noteworthy details.
- **Time Efficiency**: Saves time by delivering the most relevant and up-to-date information in a summarized format.

## Usage

1. **Select Channels**: Specify the YouTube channels you want to track.
2. **Receive Summaries**: Get daily summaries of the latest videos from those channels.
3. **Text Readability**: Access full-text versions of video content for quick reading.
4. **Key Overlaps**: Discover common themes and insights across the selected channels.

Stay informed without spending hours watching videos. Let YouTube Daily Summarizer do the work for you!


## Programs
This repository contains four main programs designed to automate the process of summarizing YouTube videos and identifying key overlaps across multiple channels.



1. **Video Downloader**
   - This program downloads videos from given URLs.

2. **Speech-to-Text Converter**
   - This program takes the downloaded videos and uses a speech-to-text model to convert the audio content into text.

3. **Video Content Summarizer**
   - This program takes the text content of videos and generates concise summaries.

4. **Key Overlaps Analyzer**
   - This program consolidates the summaries of multiple videos.
   - It identifies key overlaps in the information presented across different channels and analyzes whether the perspectives on these key points are consistent or varied.


### Automated Pipeline

- **Tracking Channels**
  - Specify the YouTube channels you want to track.
  - The pipeline will automatically download new daily videos from these channels, convert the audio to text, and generate summaries.
  - The output will include the full text content and summaries of the videos.

- **Key Overlaps Analysis**
  - Specify multiple channels for key overlaps analysis.
  - The pipeline will analyze the daily video summaries from these channels to identify key overlaps and compare the perspectives across the channels.

By automating the download, transcription, summarization, and analysis processes, the YouTube Daily Summarizer saves time and helps you stay informed with concise and relevant information.
