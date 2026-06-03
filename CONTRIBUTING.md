# Contributing to MediScenario

Thank you for your interest in contributing to MediScenario! We welcome contributions from medical professionals, developers, educators, and students.

## Code of Conduct

Please be respectful and constructive in all interactions. We're building a supportive community for medical education.

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/medhunanush04-max/MediScenario/issues)
2. If not, create a new issue with:
   - Clear title describing the bug
   - Detailed description and steps to reproduce
   - Expected vs actual behavior
   - Screenshots if applicable
   - Your environment (OS, Node version, etc.)

### Suggesting Features

1. Check [Issues](https://github.com/medhunanush04-max/MediScenario/issues) for similar suggestions
2. Create a new issue with:
   - Clear title describing the feature
   - Detailed explanation of the use case
   - Why this feature would be valuable
   - Suggested implementation (if you have ideas)

### Submitting Pull Requests

1. **Fork** the repository
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** following our coding standards
4. **Write or update tests** as needed
5. **Commit with clear messages**
   ```bash
   git commit -m "Add feature: brief description"
   ```
6. **Push to your branch**
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Open a Pull Request** with:
   - Clear description of changes
   - Link to related issue (if applicable)
   - Screenshots/demos if applicable

## Development Setup

### Prerequisites
- Node.js 18+
- Python 3.9+
- PostgreSQL 13+
- Docker (recommended)

### Local Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/MediScenario.git
cd MediScenario

# Install dependencies
npm install          # Frontend
pip install -r requirements.txt  # Backend

# Set up environment
cp .env.example .env
# Edit .env with your local configuration

# Start development server
docker-compose up
```

## Coding Standards

### JavaScript/TypeScript
- Use ESLint configuration
- Follow Prettier formatting
- Use meaningful variable names
- Add JSDoc comments for functions

### Python
- Follow PEP 8 style guide
- Use type hints
- Add docstrings to functions and classes
- Use Black for formatting

### Git Commit Messages
- Use imperative mood ("Add feature" not "Added feature")
- Keep first line under 50 characters
- Reference issues: "Fix #123"
- Example: "Add drug interaction checker for beta-blockers"

## Testing

Before submitting a PR:

```bash
# Run frontend tests
npm test

# Run backend tests
python -m pytest

# Check linting
npm run lint
python -m pylint app/
```

## Documentation

If adding a new feature:
1. Update README.md if it's user-facing
2. Add code comments for complex logic
3. Update API documentation
4. Add usage examples where applicable

## Areas We Need Help With

- **Medical Content:** Drug interactions, disease management protocols
- **Frontend Development:** UI/UX improvements, responsive design
- **Backend Development:** API optimization, database design
- **AI/ML:** Case generation algorithms, NLP models
- **Documentation:** Tutorials, setup guides, API docs
- **Testing:** Test coverage, bug hunting

## Questions?

- Open a [Discussion](https://github.com/medhunanush04-max/MediScenario/discussions)
- Check existing [Issues](https://github.com/medhunanush04-max/MediScenario/issues)
- Email: contact@mediscenario.dev (when available)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for making medical education better!** ❤️