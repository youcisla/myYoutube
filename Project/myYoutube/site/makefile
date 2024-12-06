clean_install:
	@echo "Removing node_modules and package-lock.json..."
	@if exist node_modules (rmdir /s /q node_modules)
	@if exist package-lock.json (del /q package-lock.json)

	@echo "Clearing npm cache..."
	npm cache clean --force || exit /b

	@echo "Installing dependencies..."
	npm install || exit /b

	@echo "Updating react-scripts to 5.0.1..."
	npm install react-scripts@5.0.1 --force || exit /b

	@echo "Installing latest svgr/webpack and resolve-url-loader..."
	npm install --save-dev @svgr/webpack@latest resolve-url-loader@latest || exit /b

	@echo "Fixing known vulnerabilities..."
	npm audit fix || exit /b

	@echo "Manually resolving remaining high-risk issues..."
	npm install --save-dev postcss@8.4.31 svgo@2.x cssnano@5.x css-loader@6.x || exit /b

	@echo "Forcing fixes for remaining vulnerabilities..."
	npm audit fix --force || exit /b

	@echo "Final audit to check for unresolved issues..."
	npm audit || echo "Some vulnerabilities may remain unresolved. Please review the logs."

	@echo "Starting application in debug mode..."
	SET DEBUG=* && npm start || exit /b
