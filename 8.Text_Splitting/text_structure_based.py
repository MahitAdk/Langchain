from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """
Space exploration has led to incredible scientific discoveries. From landing on the Moon to exploring Mars, humanity continues to push the boundaries of what’s possible beyond our planet.

These missions have not only expanded our knowledge of the universe but have also contributed to advancements in technology here on Earth. Satellite communications, GPS, and even certain medical imaging techniques trace their roots back to innovations driven by space programs.
"""

#Rest same as before(length based text splitter)

splitter= RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=0,#How many characters to overlap between chunks
)

chunk=splitter.split_text(text)

print(chunk)
# Output will be a list of text chunks, each with a maximum length of 500 characters

#This is the most used text splitter in LangChain, as it is more efficient and effective for most use cases.
