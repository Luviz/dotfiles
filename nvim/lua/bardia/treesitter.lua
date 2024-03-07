local treesitter_status_ok, treesitter = pcall(require, "nvim-treesitter.configs")
if not treesitter_status_ok then
  return
end

treesitter.setup {
	ensure_installed = { "c", "lua", "vim", "vimdoc", "query", "typescript", "javascript", "markdown" },
}
