
# Locust Advanced Load Testing Project

This repository demonstrates advanced load testing techniques using **Locust**, with a focus on modular design, data-driven testing, and real-time monitoring.

## Features
1. **Test Scenarios**:
   - Login and authentication (parameterized with CSV data).
   - List and create operations on endpoints.
2. **Design Patterns**:
   - Factory Pattern: Dynamic payload generation.
   - Modular Utilities: For assertions and reusable components.
3. **Monitoring and Metrics**:
   - Preconfigured **Prometheus** scrape configuration.
   - Grafana dashboard for real-time visualization of metrics.
4. **Data-Driven Testing**:
   - Parameterized tests with external CSV files.
5. **Reporting**:
   - Export results in JSON and HTML formats.

## Project Structure
```
locust-final-load-testing/
├── scripts/      # Locust test scenarios
├── config/       # Prometheus and environment configurations
├── data/         # External data files (CSV/JSON)
├── utils/        # Utility functions (payload creation, assertions)
├── results/      # Test results
├── dashboard/    # Grafana dashboard JSON configuration
├── reports/      # HTML/JSON reports
└── README.md     # Documentation
```

## Getting Started

### Prerequisites
1. Install Python 3.8 or later.
2. Install Locust:
   ```bash
   pip install locust
   ```

### Running the Tests
1. Run Locust in headless mode:
   ```bash
   locust -f scripts/complete_test.py --headless -u 10 -r 2 --run-time 5m
   ```
2. Run Locust with the Web UI:
   ```bash
   locust -f scripts/complete_test.py
   ```

3. Access the Web UI at `http://localhost:8089`.

## Monitoring
1. Install **Prometheus** and **Grafana**.
2. Use `config/prometheus.yml` for Prometheus setup.
3. Import `dashboard/grafana_dashboard.json` into Grafana.

## Example Results
After running tests, results can be exported to JSON or HTML:
```bash
locust -f scripts/complete_test.py --headless --html=reports/report.html --json=results/results.json
```

## Contributing
Contributions are welcome! Open issues or submit pull requests to improve this repository.

## License
This project is licensed under the MIT License.

---

Happy Load Testing! 🚀
