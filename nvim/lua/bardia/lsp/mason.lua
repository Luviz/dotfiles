
local servers = {
  "lua_ls",
  "pyright",
  "jsonls",
  "tsserver",
}

local settings = {
	ui = {
		border = "none",
		icons = {
			package_installed = "◍",
			package_pending = "◍",
			package_uninstalled = "◍",
		},
	},
	log_level = vim.log.levels.INFO,
	max_concurrent_installers = 4,
}

require("mason").setup(settings)
require("mason-lspconfig").setup({
	ensure_installed = servers,
	automatic_installation = true,
})

local lspconfig_status_ok, lspconfig = pcall(require, "lspconfig")
if not lspconfig_status_ok then
	return
end

local opts = {}

for _, server in pairs(servers) do
	opts = {
		on_attach = require("bardia.lsp.handlers").on_attach,
		capabilities = require("bardia.lsp.handlers").capabilities,
	}

	local server_name = vim.split(server, "@")[1]
  local path = "bardia.lsp.settings." .. server_name
	local require_ok, conf_opts = pcall(require, path)
	if require_ok then
		opts = vim.tbl_deep_extend("force", conf_opts, opts)
	end

	lspconfig[server].setup(opts)
end