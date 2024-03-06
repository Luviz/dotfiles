local function bootstrap_pckr()
  local pckr_path = vim.fn.stdpath("data") .. "/pckr/pckr.nvim"

  if not vim.loop.fs_stat(pckr_path) then
    vim.fn.system({
      'git',
      'clone',
      "--filter=blob:none",
      'https://github.com/lewis6991/pckr.nvim',
      pckr_path
    })
  end

  vim.opt.rtp:prepend(pckr_path)
end

bootstrap_pckr()

require('pckr').add {
  'Mofiqul/vscode.nvim';
  {
      "nvim-neo-tree/neo-tree.nvim",
      branch = "v3.x",
      requires = {
        "nvim-lua/plenary.nvim",
        "nvim-tree/nvim-web-devicons", -- not strictly required, but recommended
        "MunifTanjim/nui.nvim",
      }
  };

  -- nvim-cmp
  "hrsh7th/nvim-cmp";                   -- The completion plugin
  "hrsh7th/cmp-buffer";                 -- buffer completions
  "hrsh7th/cmp-path";                   -- path completions
  "hrsh7th/cmp-cmdline";                -- cmdline completions
  "saadparwaiz1/cmp_luasnip";           -- snippet completions

  -- snippets
  "L3MON4D3/LuaSnip";                   -- lua snippets
  "rafamadriz/friendly-snippets";       -- a bunch of snippets to use


  -- LSP
  "neovim/nvim-lspconfig";              -- enable LSP
  "williamboman/mason.nvim";            -- simple to use language server installer
  "williamboman/mason-lspconfig.nvim";  -- simple to use language server installer
  "jose-elias-alvarez/null-ls.nvim";    -- LSP diagnostics and code actions

  -- treesitter
  {
    "nvim-treesitter/nvim-treesitter",
    build = ":TSUpdate",
  };
}

