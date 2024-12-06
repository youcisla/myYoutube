start:
	@if exist node_modules (rmdir /s /q node_modules)
	@if exist package-lock.json (del /q package-lock.json)
	npm cache clean --force
	npm install
	npm install react-scripts@5.0.1 --force
	npm install --save-dev @svgr/webpack@latest resolve-url-loader@latest
	npm install --save-dev postcss@8.4.31 svgo@2.x cssnano@5.x css-loader@6.x
	rm -rf .babel-cache.json
	npm install --save-dev @babel/core @babel/cli @babel/preset-env
	npx babel src --out-dir dist --verbose
	npm install nth-check@latest postcss@latest
	npm prune
	npm uninstall rollup-plugin-terser
	npm install @rollup/plugin-terser
	npm audit fix --force
	SET DEBUG=* && npm start
