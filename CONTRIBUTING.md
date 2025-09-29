# Contributing to Django Modular System

Thank you for your interest in contributing to the Django Modular System! We welcome contributions from the community.

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/ridwaanhall/django-app-modular/issues)
2. If not, create a new issue with:
   - Clear description of the problem
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (Python version, Django version, OS)

### Suggesting Features

1. Check [Issues](https://github.com/ridwaanhall/django-app-modular/issues) for existing feature requests
2. Create a new issue with:
   - Clear description of the feature
   - Use cases and benefits
   - Proposed implementation approach (if any)

### Contributing Code

1. **Fork the repository**
   ```bash
   git clone https://github.com/your-username/django-app-modular.git
   cd django-app-modular
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make your changes**
   - Write clear, concise code
   - Follow PEP 8 style guidelines
   - Add docstrings to functions and classes
   - Include type hints where appropriate

5. **Add tests**
   - Write unit tests for new functionality
   - Ensure existing tests still pass
   ```bash
   python manage.py test
   ```

6. **Update documentation**
   - Update README.md if needed
   - Add docstrings and comments
   - Update API documentation

7. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add feature: your feature description"
   ```

8. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

9. **Create a Pull Request**
   - Provide a clear description of changes
   - Reference any related issues
   - Include screenshots for UI changes

### Code Style Guidelines

- **Python**: Follow PEP 8
- **Django**: Follow Django coding style
- **HTML/CSS**: Use consistent indentation (2 spaces)
- **JavaScript**: Use modern ES6+ syntax

### Testing

- Write unit tests for all new functionality
- Maintain test coverage above 80%
- Test both positive and negative scenarios
- Include integration tests for complex features

### Documentation

- Update README.md for significant changes
- Add docstrings to all public functions and classes
- Include code examples in documentation
- Keep documentation up to date with code changes

## Code Review Process

1. All submissions require review before merging
2. We may suggest changes or improvements
3. Once approved, your PR will be merged
4. We'll update the changelog and version as needed

## Community Guidelines

- Be respectful and inclusive
- Provide constructive feedback
- Help others learn and grow
- Follow the [Code of Conduct](CODE_OF_CONDUCT.md)

## Development Setup

For detailed development setup instructions, see the main [README.md](README.md#installation).

## Questions?

Feel free to open an issue for any questions or reach out to the maintainers.

Thank you for contributing! 🎉