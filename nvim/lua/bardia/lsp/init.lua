local status_ok, _ = pcall(require, "lspconfig")
if not status_ok then
  return
end

require "bardia.lsp.mason"
require("bardia.lsp.handlers").setup()
require "bardia.lsp.null-ls"
