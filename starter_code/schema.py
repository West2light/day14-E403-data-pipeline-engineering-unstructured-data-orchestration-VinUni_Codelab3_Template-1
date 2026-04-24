from pydantic import BaseModel, Field

# ==========================================
# ROLE 1: LEAD DATA ARCHITECT
# ==========================================

class UnifiedDocument(BaseModel):
    """
    Schema chuẩn hóa duy nhất cho toàn bộ pipeline.
    Hợp nhất dữ liệu từ 2 nguồn:
      - Group A (PDF/OCR):   docId, authorName, docCategory, extractedText, createdAt
      - Group B (Video/STT): video_id, creator_name, category, transcript, published_timestamp
    """

    document_id: str = Field(...)
    source_type: str = Field(...)
    author: str = Field(...)
    category: str = Field(...)
    content: str = Field(...)
    timestamp: str = Field(...)
