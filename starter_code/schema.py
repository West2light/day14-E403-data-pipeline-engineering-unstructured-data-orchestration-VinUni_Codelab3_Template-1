from pydantic import BaseModel, Field
from typing import Optional

# ==========================================
# ROLE 1: LEAD DATA ARCHITECT
# ==========================================

class UnifiedDocument(BaseModel):
    """
    Schema chuẩn hóa duy nhất cho toàn bộ pipeline.
    Hợp nhất dữ liệu từ 2 nguồn:
      - Group A (PDF/OCR):   docId, authorName, docCategory, extractedText, createdAt
      - Group B (Video/STT): video_id, creator_name, category, transcript, published_timestamp

    Tất cả đều được ánh xạ vào 6 trường chuẩn dưới đây.
    """

    # Định danh duy nhất của tài liệu (pdf-001, vid_993, ...)
    document_id: str

    # Loại nguồn dữ liệu: "pdf" hoặc "video"
    source_type: str

    # Tác giả / người tạo. Dùng Optional để xử lý tài liệu thiếu trường này.
    author: Optional[str] = "unknown"

    # Chủ đề / danh mục nội dung
    category: Optional[str] = "unknown"

    # Nội dung văn bản chính (đã được làm sạch Header/Footer ở bước ETL)
    content: Optional[str] = ""

    # Thời điểm tạo / phát hành (lưu dạng str để chấp nhận nhiều format)
    timestamp: Optional[str] = "unknown"
