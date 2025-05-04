
# Semantic Search with BERT and Elasticsearch

This project implements a **semantic search engine** using **BERT embeddings** and **Elasticsearch**. It allows users to search for products in a catalog based on the semantic meaning of their queries, rather than relying on exact keyword matches.

---

## Features

- **Semantic Search**: Uses BERT-based embeddings to find relevant products based on query meaning.
- **Elasticsearch Integration**: Stores product data and performs k-Nearest Neighbors (k-NN) search for vector similarity.
- **Streamlit Interface**: Provides an interactive web interface for users to input search queries and view results.
- **Data Preprocessing**: Handles missing values and converts product descriptions into dense vector embeddings.
- **Custom Index Mapping**: Configures Elasticsearch to store dense vectors and other product attributes.

---

## Project Structure

- **`indexData.ipynb`**: Jupyter Notebook for data preprocessing, vector generation, and indexing data into Elasticsearch.
- **`searchApp.py`**: Streamlit application for the semantic search interface.
- **`index_Mapping.py`**: Defines the Elasticsearch index mapping, including fields for dense vectors.
- **`.gitignore`**: Specifies files and directories to exclude from version control (e.g., virtual environments, logs, checkpoints).

---

## Requirements

- Python 3.8+
- Elasticsearch 7.3+ with the k-NN plugin installed
- Virtual environment (recommended)

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd Semantic_Search_Vector(BERT)_Embadding
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # OR
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Start Elasticsearch**:
   - Ensure Elasticsearch is running locally with the k-NN plugin installed.

---

## Usage

### 1. **Index Data into Elasticsearch**
   - Open `indexData.ipynb` in Jupyter Notebook.
   - Run the cells to preprocess the data, generate embeddings, and index the data into Elasticsearch.

### 2. **Run the Search Application**
   - Start the Streamlit app:
     ```bash
     streamlit run searchApp.py
     ```
   - Open the provided URL (e.g., `http://localhost:8501`) in your browser.

### 3. **Search for Products**
   - Enter a search query (e.g., "Blue Shoes") in the Streamlit app.
   - View the top matching products based on semantic similarity.

---

## File Descriptions

- **`indexData.ipynb`**: 
  - Preprocesses the product catalog.
  - Generates dense vector embeddings using the `SentenceTransformer` model.
  - Indexes the data into Elasticsearch.

- **`searchApp.py`**:
  - Implements the Streamlit-based user interface for semantic search.
  - Queries Elasticsearch using k-NN search to retrieve relevant products.

- **`index_Mapping.py`**:
  - Defines the Elasticsearch index mapping, including fields for text, numeric data, and dense vectors.

- **`.gitignore`**:
  - Excludes unnecessary files (e.g., virtual environments, logs) from version control.

---

## Example Query

- **Input**: `"Blue Shoes"`
- **Output**: A list of products with similar descriptions, including their names and details.

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- [Elasticsearch](https://www.elastic.co/)
- [SentenceTransformers](https://www.sbert.net/)
- [Streamlit](https://streamlit.io/)
```

Replace `<repository-url>` with the URL of your Git repository. Save this content in a file named `README.md` in the root of your repository.Replace `<repository-url>` with the URL of your Git repository. Save this content in a file named `README.md` in the root of your repository.
