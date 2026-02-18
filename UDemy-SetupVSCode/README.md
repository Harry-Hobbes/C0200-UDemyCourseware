# VS Code Setup - Udemy Course

Learn how to install, configure, and optimize Visual Studio Code for development.

## Overview

This folder contains materials from the Udemy "VS Code Setup" course, covering the complete setup and configuration of Visual Studio Code for modern development workflows.

## Course Contents

- **README.md** — Course overview and learning resources

## Topics Covered

- Installing VS Code on Windows, macOS, and Linux
- Initial configuration and user settings
- Installing and managing extensions
- Terminal setup and configuration
- Theme and appearance customization
- Keyboard shortcuts and productivity tips
- Debugging configuration
- Git and version control integration
- Workspace and folder management
- Performance optimization

## Getting Started

1. **Download VS Code:**
   - Visit [https://code.visualstudio.com/](https://code.visualstudio.com/)
   - Download the installer for your operating system

2. **Follow the course:**
   - Watch installation and setup videos
   - Apply each configuration step to your VS Code installation
   - Customize settings to match your preferences

3. **Explore the interface:**
   - Activity Bar (left side)
   - Explorer, Search, Source Control, Run & Debug, Extensions
   - Editor, Sidebar, Terminal, and Status Bar

## Essential Extensions

After setup, consider installing these popular extensions:

- **Python** — Microsoft's official Python extension
- **Prettier** — Code formatter for JavaScript, TypeScript, CSS
- **ESLint** — JavaScript linter
- **GitLens** — Git integration and history
- **Markdown Preview Enhanced** — Better Markdown rendering
- **Thunder Client** or **REST Client** — API testing
- **Docker** — Docker container support

## Key Settings to Customize

1. **Theme:** `Preferences > Color Theme`
2. **Font:** Settings > Font Family and Font Size
3. **Format on Save:** Settings > Format On Save (recommended)
4. **Auto Save:** Settings > Auto Save
5. **Indentation:** Settings > Indent Size (2 or 4 spaces)

## Useful Keyboard Shortcuts

| Action | Windows | macOS |
|--------|---------|-------|
| Command Palette | `Ctrl+Shift+P` | `Cmd+Shift+P` |
| Open Folder | `Ctrl+K Ctrl+O` | `Cmd+K Cmd+O` |
| Toggle Terminal | `` Ctrl+` `` | `` Cmd+` `` |
| Split Editor | `Ctrl+\` | `Cmd+\` |
| Find | `Ctrl+F` | `Cmd+F` |
| Replace | `Ctrl+H` | `Cmd+H` |
| Format Document | `Shift+Alt+F` | `Shift+Option+F` |
| Quick Fix | `Ctrl+.` | `Cmd+.` |
| Go to Line | `Ctrl+G` | `Cmd+G` |

## Settings Recommendation

For beginners, these settings provide a good foundation:

```json
{
  "editor.fontSize": 14,
  "editor.tabSize": 2,
  "editor.formatOnSave": true,
  "editor.wordWrap": "on",
  "files.autoSave": "afterDelay",
  "files.autoSaveDelay": 1000,
  "[python]": {
    "editor.defaultFormatter": "ms-python.python"
  }
}
```

## Workspace Tips

- **Multi-root workspaces:** Open multiple folders in one workspace
- **Settings:** Project-specific settings in `.vscode/settings.json`
- **Launch configurations:** Debug setups in `.vscode/launch.json`
- **Tasks:** Automated tasks in `.vscode/tasks.json`

## Resources

- [Official VS Code Documentation](https://code.visualstudio.com/docs)
- [Settings Reference](https://code.visualstudio.com/docs/getstarted/settings)
- [Keyboard Shortcuts](https://code.visualstudio.com/docs/getstarted/keybindings)
- [Extensions Marketplace](https://marketplace.visualstudio.com/)

## Troubleshooting

- **Extensions not loading:** Try restarting VS Code
- **Performance issues:** Disable unused extensions
- **Terminal not working:** Check settings > terminal.integrated.shell
- **Git not recognized:** Ensure Git is installed and added to PATH

---

Last updated: 2026-02-18
