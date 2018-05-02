#!/usr/bin/env python

class StringUtils:
  
  @staticmethod
  def str_to_chunks(string, chunk_size):
    chunks = []
    for i in range(0, StringUtils.number_of_chunks_in_string(string, chunk_size)):
      chunks.append(string[i:i+chunk_size])
    return chunks

  @staticmethod
  def number_of_chunks_in_string(string, chunk_size):
    return len(string) - (chunk_size - 1)