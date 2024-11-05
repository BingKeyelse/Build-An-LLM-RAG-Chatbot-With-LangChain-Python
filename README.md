# 🤖 Xây Dựng Chatbot AI với LangChain và Python

## RAG PIPELINE
<p align="center">
  <img src="https://media.licdn.com/dms/image/v2/D4D22AQHhEYuJKGao6A/feedshare-shrink_1280/feedshare-shrink_1280/0/1710748558987?e=1733356800&v=beta&t=5MXnGzPFdue8HbgT2_GFFKT_4qPuz14jqdCsK9MosFo" alt="rag" width="400"/>
</p>


## 📋 Yêu cầu hệ thống

- Python 3.8 trở lên (Tải tại: https://www.python.org/downloads/)
- Docker Desktop (Tải tại: https://www.docker.com/products/docker-desktop/)
- OpenAI API key (Đăng ký tại: https://platform.openai.com/api-keys)
- Khoảng 4GB RAM trống

## 🚀 Các bước cài đặt và chạy

### Bước 1: Cài đặt thư viện Python

Mở Terminal/Command Prompt và chạy lệnh sau:
pip install langchain langchain-core langchain-community langchain-openai python-dotenv beautifulsoup4 langchain_milvus streamlit rank_bm25

> 💡 Nếu gặp lỗi thiếu thư viện, chạy: `pip install tên-thư-viện-còn-thiếu`

### Bước 2: Cài đặt và chạy Milvus Database

1. Khởi động Docker Desktop
2. Mở Terminal/Command Prompt, chạy lệnh:
   docker compose up --build

> ⚠️ Đợi đến khi thấy thông báo "Milvus is ready"

### Bước 3: Cấu hình OpenAI API

1. Tạo file `.env` trong thư mục `src`
2. Thêm API key vào file:
   OPENAI_API_KEY=sk-your-api-key-here

### Bước 4: Chạy ứng dụng

Mở Terminal/Command Prompt, di chuyển vào thư mục src và chạy:

1. cd src
2. streamlit run main.py

## 💻 Cách sử dụng

### 1. Tải dữ liệu (Chọn 1 trong 2 cách)

**Cách 1: Từ file local**

1. Ở sidebar bên trái, chọn "File Local"
2. Nhập tên file JSON (mặc định: stack.json)
3. Nhập tên thư mục (mặc định: data)
4. Nhấn "Tải dữ liệu từ file"

**Cách 2: Từ URL**

1. Ở sidebar bên trái, chọn "URL trực tiếp"
2. Nhập URL cần lấy dữ liệu
3. Nhấn "Crawl dữ liệu"

### 2. Chat với AI

- Nhập câu hỏi vào ô chat ở dưới màn hình
- Nhấn Enter hoặc nút gửi
- Đợi AI trả lời

## ❗ Xử lý lỗi thường gặp

### 1. Lỗi cài đặt thư viện

- **Lỗi:** `ModuleNotFoundError`
- **Cách xử lý:** Chạy lại lệnh pip install cho thư viện bị thiếu

### 2. Lỗi Docker/Milvus

- **Lỗi:** Không kết nối được Milvus
- **Cách xử lý:**
  1. Kiểm tra Docker Desktop đang chạy
  2. Chạy lệnh: `docker compose down`
  3. Chạy lại: `docker compose up --build`

### 3. Lỗi OpenAI API

- **Lỗi:** Invalid API key
- **Cách xử lý:**
  1. Kiểm tra file .env đúng định dạng
  2. Xác nhận API key còn hiệu lực
  3. Kiểm tra kết nối internet

### 4. Lỗi khi tải dữ liệu

- **Lỗi:** Không tải được dữ liệu
- **Cách xử lý:**
  1. Kiểm tra đường dẫn file/URL
  2. Xác nhận file JSON đúng định dạng
  3. Kiểm tra quyền truy cập thư mục

## 💡 Lưu ý quan trọng

- Docker Desktop phải luôn chạy khi sử dụng ứng dụng
- Không chia sẻ OpenAI API key với người khác
- Nên tải dữ liệu trước khi bắt đầu chat
- AI có thể mất vài giây để xử lý câu trả lời
- Nếu ứng dụng bị lỗi, thử refresh trang web

## 🆘 Cần hỗ trợ?

Nếu gặp vấn đề:

1. Chụp màn hình lỗi
2. Mô tả các bước dẫn đến lỗi
3. Tạo issue trên GitHub

## 📚 Tài liệu tham khảo

- LangChain: https://python.langchain.com/docs/introduction/
  - Agents: https://python.langchain.com/docs/tutorials/qa_chat_history/#tying-it-together-1
  - BM25: https://python.langchain.com/docs/integrations/retrievers/bm25/#create-a-new-retriever-with-documents
  - How to combine results from multiple retrievers: https://python.langchain.com/docs/how_to/ensemble_retriever/
  - Langchain Milvus: https://python.langchain.com/docs/integrations/vectorstores/milvus/#initialization
  - Recursive URL: https://python.langchain.com/docs/integrations/document_loaders/recursive_url/#overview
  - Langchain Streamlit: https://python.langchain.com/docs/integrations/callbacks/streamlit/#installation-and-setup
  - Langchain Streamlit: https://python.langchain.com/docs/integrations/providers/streamlit/#memory
- Milvus Standalone: https://milvus.io/docs/v2.0.x/install_standalone-docker.md
  - Attu: https://github.com/zilliztech/attu
- Streamlit Documentation: https://docs.streamlit.io/
- OpenAI API: https://platform.openai.com/docs
