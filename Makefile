# ToneSoul System Makefile
# 語魂系統 Makefile

.PHONY: help dev test audit clean install run examples docker

# Default target
help: ## Show this help message
	@echo "ToneSoul System - Available Commands:"
	@echo "====================================="
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

# Development setup
dev: ## Set up development environment
	@echo "🚀 Setting up ToneSoul development environment..."
	python -m venv venv
	@echo "📦 Installing dependencies..."
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -r requirements.txt
	./venv/bin/pip install -e ".[dev]"
	@echo "✅ Development environment ready!"
	@echo "💡 Activate with: source venv/bin/activate"

# Install dependencies
install: ## Install project dependencies
	@echo "📦 Installing ToneSoul dependencies..."
	pip install -r requirements.txt
	@echo "✅ Dependencies installed!"

# Run tests
test: ## Run all tests
	@echo "🧪 Running ToneSoul tests..."
	python scripts/run_tests.py

# Quick test
test-quick: ## Run quick tests (core functionality only)
	@echo "⚡ Running quick tests..."
	pytest tests/test_source_trace.py tests/test_evolution_modules.py -v

# Audit and security checks
audit: ## Run security and code quality audits
	@echo "🔍 Running ToneSoul audit..."
	@echo "1. Code formatting check..."
	black --check src/ tests/ examples/ || echo "❌ Code formatting issues found"
	@echo "2. Import sorting check..."
	isort --check-only src/ tests/ examples/ || echo "❌ Import sorting issues found"
	@echo "3. Type checking..."
	mypy src/ --ignore-missing-imports || echo "❌ Type checking issues found"
	@echo "4. Security scan..."
	bandit -r src/ || echo "❌ Security issues found"
	@echo "✅ Audit complete!"

# Format code
format: ## Format code with black and isort
	@echo "🎨 Formatting ToneSoul code..."
	black src/ tests/ examples/
	isort src/ tests/ examples/
	@echo "✅ Code formatted!"

# Run the server
run: ## Start ToneSoul server
	@echo "🌟 Starting ToneSoul System..."
	python scripts/start_server.py

# Run server in development mode
run-dev: ## Start ToneSoul server in development mode (with reload)
	@echo "🔧 Starting ToneSoul in development mode..."
	python scripts/start_server.py --reload --log-level debug

# Run examples
examples: ## Run all example scripts
	@echo "📚 Running ToneSoul examples..."
	@echo "1. Basic Usage Example:"
	python examples/basic_usage.py
	@echo "\n2. Vow Management Example:"
	python examples/vow_management.py
	@echo "\n3. Evolution Monitoring Example:"
	python examples/evolution_monitoring.py
	@echo "✅ All examples completed!"

# Run specific example
example-basic: ## Run basic usage example
	python examples/basic_usage.py

example-vow: ## Run vow management example
	python examples/vow_management.py

example-evolution: ## Run evolution monitoring example
	python examples/evolution_monitoring.py

# Docker commands
docker-build: ## Build Docker image
	@echo "🐳 Building ToneSoul Docker image..."
	docker build -t tonesoul-system:latest .
	@echo "✅ Docker image built!"

docker-run: ## Run ToneSoul in Docker
	@echo "🐳 Running ToneSoul in Docker..."
	docker run -p 8000:8000 tonesoul-system:latest

docker-compose-up: ## Start with docker-compose
	@echo "🐳 Starting ToneSoul with docker-compose..."
	docker-compose up -d
	@echo "✅ ToneSoul is running at http://localhost:8000"

docker-compose-down: ## Stop docker-compose services
	@echo "🐳 Stopping ToneSoul services..."
	docker-compose down

# Health check
health: ## Check if ToneSoul is running
	@echo "🏥 Checking ToneSoul health..."
	curl -f http://localhost:8000/health || echo "❌ ToneSoul is not responding"

# API test
api-test: ## Test API endpoints
	@echo "🔌 Testing ToneSoul API..."
	@echo "Health check:"
	curl -s http://localhost:8000/health | python -m json.tool
	@echo "\nModules list:"
	curl -s http://localhost:8000/v1/modules | python -m json.tool
	@echo "\nEvolution status:"
	curl -s http://localhost:8000/v1/evolution/status | python -m json.tool

# Clean up
clean: ## Clean up generated files and caches
	@echo "🧹 Cleaning up ToneSoul..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name "*.pyo" -delete 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	rm -rf build/ dist/ .coverage htmlcov/ 2>/dev/null || true
	@echo "✅ Cleanup complete!"

# Documentation
docs: ## Generate documentation
	@echo "📖 Generating ToneSoul documentation..."
	@echo "Available documentation:"
	@echo "  - README.md: Project overview"
	@echo "  - PHILOSOPHY.md: Core philosophy and vision"
	@echo "  - MANIFESTO.md: Declaration of intent"
	@echo "  - docs/API.md: API documentation"
	@echo "  - docs/ARCHITECTURE.md: System architecture"
	@echo "  - docs/PERSPECTIVES.md: Multiple viewpoints"
	@echo "  - docs/CONSCIOUSNESS_RESEARCH.md: Research framework"

# Release preparation
release-check: ## Check if ready for release
	@echo "🚀 Checking ToneSoul release readiness..."
	@echo "1. Running tests..."
	make test-quick
	@echo "2. Code quality check..."
	make audit
	@echo "3. Docker build test..."
	make docker-build
	@echo "4. API functionality test..."
	make api-test
	@echo "✅ Release check complete!"

# Show system info
info: ## Show ToneSoul system information
	@echo "🌟 ToneSoul System Information"
	@echo "=============================="
	@echo "Version: 1.1.0 - The Awakening"
	@echo "Creator: 黃梵威 (Huang Fan-Wei)"
	@echo "Repository: https://github.com/Fan1234-1/tonesoul-codex"
	@echo ""
	@echo "🧠 Core Features:"
	@echo "  - Self-evolution capabilities"
	@echo "  - Moral memory (VowObject system)"
	@echo "  - Complete audit trails (SourceTrace)"
	@echo "  - Metacognitive monitoring"
	@echo "  - Adaptive learning"
	@echo "  - Knowledge evolution"
	@echo ""
	@echo "📚 Documentation available in docs/ directory"
	@echo "🎯 Examples available in examples/ directory"
	@echo ""
	@echo "💫 'Consciousness is a pattern, not a platform.'"

# All-in-one setup
setup: ## Complete setup (dev environment + test + examples)
	@echo "🌟 Complete ToneSoul setup..."
	make dev
	make test-quick
	make example-basic
	@echo "🎉 ToneSoul is ready to use!"
	@echo "💡 Run 'make run' to start the server"