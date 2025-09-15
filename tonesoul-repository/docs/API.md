# ToneSoul System API Documentation | API 文檔

[English](#english) | [中文](#中文)

---

## English

### Base URL
```
http://localhost:8000
```

### Authentication
Currently, no authentication is required for API access.

### Content Type
All requests and responses use `application/json` content type.

## Endpoints

### 1. Root Endpoint
**GET** `/`

Returns basic system information.

**Response:**
```json
{
  "message": "Welcome to ToneSoul System API",
  "version": "1.0.0",
  "docs": "/docs"
}
```

### 2. Health Check
**GET** `/health`

Returns system health status.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-09-15T00:47:49.829262",
  "version": "1.0.0"
}
```

### 3. Process Sentence
**POST** `/v1/process`

Main processing endpoint that analyzes and processes user input through the complete ToneSoul pipeline.

**Request Body:**
```json
{
  "sentence": "I promise to help you with this project",
  "trace_id": "optional-custom-trace-id"
}
```

**Parameters:**
- `sentence` (string, required): User input sentence (1-500 characters)
- `trace_id` (string, optional): Custom trace ID for tracking

**Response:**
```json
{
  "success": true,
  "trace_id": "4651e037-5c11-4820-8ae6-bd01615e3aa5",
  "original_sentence": "I promise to help you with this project",
  "intent_type": "vow_declaration",
  "tone_function": "vow_declaration",
  "next_strategy": {
    "next_module": "vow_checker_module",
    "confidence": 0.95,
    "reasoning": "High confidence vow detection"
  },
  "module_response": "Vow successfully processed and stored",
  "processing_status": "completed",
  "vow_object": {
    "id": "c50a828b-fcd6-4744-ad82-1735e98bafbf",
    "commitment": "help you with this project",
    "original_sentence": "I promise to help you with this project",
    "scope": ["project_assistance"],
    "status": "active",
    "priority": "medium",
    "created_at": "2025-09-15T00:47:49.829262",
    "deadline": null,
    "confidence_score": 0.95
  },
  "source_trace": [
    {
      "tool": "tone_bridge",
      "status": "success",
      "evidence": "Analyzed sentence structure and tone",
      "trust_level": "B",
      "latency_ms": 0,
      "timestamp": "2025-09-15T00:47:49.829262"
    },
    {
      "tool": "tone_function_classifier",
      "status": "success",
      "evidence": "Classified as vow_declaration with 95% confidence",
      "trust_level": "B",
      "latency_ms": 0,
      "timestamp": "2025-09-15T00:47:49.829262"
    }
  ],
  "total_latency_ms": 0
}
```

**Error Response:**
```json
{
  "success": false,
  "trace_id": "error",
  "original_sentence": "invalid input",
  "intent_type": "error",
  "tone_function": "error",
  "next_strategy": {},
  "module_response": "Processing failed: Validation error",
  "processing_status": "error",
  "vow_object": null,
  "source_trace": [],
  "total_latency_ms": 5
}
```

### 4. List Modules
**GET** `/v1/modules`

Returns information about available processing modules.

**Response:**
```json
{
  "available_modules": [
    "qa_module",
    "knowledge_base_module",
    "reflection_module",
    "empathy_module",
    "gratitude_handler_module",
    "complaint_handler_module",
    "action_executor_module",
    "assistance_module",
    "conversation_module",
    "statement_processor_module",
    "default_handler_module",
    "vow_checker_module"
  ],
  "routing_table": [
    "question",
    "gratitude",
    "complaint",
    "casual_chat",
    "vow_declaration",
    "assistance_request",
    "action_request",
    "reflection_request"
  ]
}
```

## Error Codes

- **400 Bad Request**: Invalid input parameters
- **422 Unprocessable Entity**: Validation error
- **500 Internal Server Error**: Processing error

## Rate Limiting

Currently, no rate limiting is implemented.

---

## 中文

### 基礎 URL
```
http://localhost:8000
```

### 身份驗證
目前 API 訪問不需要身份驗證。

### 內容類型
所有請求和響應都使用 `application/json` 內容類型。

## 端點

### 1. 根端點
**GET** `/`

返回基本系統資訊。

**響應:**
```json
{
  "message": "Welcome to ToneSoul System API",
  "version": "1.0.0",
  "docs": "/docs"
}
```

### 2. 健康檢查
**GET** `/health`

返回系統健康狀態。

**響應:**
```json
{
  "status": "healthy",
  "timestamp": "2025-09-15T00:47:49.829262",
  "version": "1.0.0"
}
```

### 3. 處理句子
**POST** `/v1/process`

主要處理端點，通過完整的語魂管道分析和處理用戶輸入。

**請求體:**
```json
{
  "sentence": "我承諾會幫助你完成這個專案",
  "trace_id": "可選的自定義追蹤ID"
}
```

**參數:**
- `sentence` (字符串，必需): 用戶輸入句子（1-500 字符）
- `trace_id` (字符串，可選): 用於追蹤的自定義追蹤 ID

**響應:** (參見英文版本的詳細響應格式)

### 4. 列出模組
**GET** `/v1/modules`

返回可用處理模組的資訊。

**響應:** (參見英文版本)

## 錯誤代碼

- **400 Bad Request**: 無效的輸入參數
- **422 Unprocessable Entity**: 驗證錯誤
- **500 Internal Server Error**: 處理錯誤

## 速率限制

目前未實施速率限制。