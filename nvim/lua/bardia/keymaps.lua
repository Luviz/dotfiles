local default_opt = { noremap = true, silent = true }
local term_opts = { silent = true }

local keymap = vim.api.nvim_set_keymap

-- Normal
-- Buffer nav
keymap("n", "<c-h>", "<c-w>h", default_opt)
keymap("n", "<c-j>", "<c-w>j", default_opt)
keymap("n", "<c-k>", "<c-w>k", default_opt)
keymap("n", "<c-l>", "<c-w>l", default_opt)

-- Buffer nav arrows
keymap("n", "<c-left>", "<c-w>h", default_opt)
keymap("n", "<c-down>", "<c-w>j", default_opt)
keymap("n", "<c-up>", "<c-w>k", default_opt)
keymap("n", "<c-right>", "<c-w>l", default_opt)

-- Visaul
-- Stay in indent mode 
keymap("v", "<", "<gv", default_opt)
keymap("v", ">", ">gv", default_opt)

-- Move text up and down
keymap("v", "<A-k>", ":m .-2<CR>==", default_opt)
keymap("v", "<A-j>", ":m .+1<CR>==", default_opt)

-- Don't overwrite yank on paste
keymap("v", "p", '"_dP', default_opt)


-- Visual Block --
-- Move text up and down
keymap("x", "J", ":move '>+1<CR>gv-gv", default_opt)
keymap("x", "K", ":move '<-2<CR>gv-gv", default_opt)
keymap("x", "<A-j>", ":move '>+1<CR>gv-gv", default_opt)
keymap("x", "<A-k>", ":move '<-2<CR>gv-gv", default_opt)

-- Terminal --
-- Better terminal navigation
keymap("t", "<C-h>", "<C-\\><C-N><C-w>h", term_opts)
keymap("t", "<C-j>", "<C-\\><C-N><C-w>j", term_opts)
keymap("t", "<C-k>", "<C-\\><C-N><C-w>k", term_opts)
keymap("t", "<C-l>", "<C-\\><C-N><C-w>l", term_opts)
