import os
import subprocess
import sys

# 检测是否管理员
def is_admin():
    try:
        return os.getuid() == 0
    except AttributeError:
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

# 执行 PowerShell 命令
def run_powershell(cmd):
    subprocess.run(["powershell", "-Command", cmd], shell=True)

# Explorer重启
def restart_explorer():
    print("[*] 正在重启 Explorer...")
    run_powershell('Stop-Process -Name explorer -Force')
    run_powershell('Start-Process explorer')
    print("[+] Explorer已重启。")

# 网络服务
def restart_network():
    print("[*] 正在重置网络...")
    run_powershell('netsh winsock reset')
    run_powershell('netsh int ip reset')
    run_powershell('Restart-Service Dhcp -ErrorAction SilentlyContinue')
    run_powershell('Restart-Service NlaSvc -ErrorAction SilentlyContinue')
    run_powershell('Restart-Service netprofm -ErrorAction SilentlyContinue')
    print("[+] 网络服务已重启。")

# 音频
def restart_audio():
    print("[*] 正在重启音频...")
    run_powershell('Restart-Service Audiosrv -ErrorAction SilentlyContinue')
    print("[+] 音频服务已重启。")

# 剪贴板
def restart_clipboard():
    print("[*] 正在重启剪贴板...")
    run_powershell('Stop-Process -Name rdpclip -Force')
    run_powershell('Start-Process rdpclip')
    print("[+] 剪贴板已重启。")

# 打印服务
def restart_print_spooler():
    print("[*] 正在重启打印服务...")
    run_powershell('Restart-Service Spooler -ErrorAction SilentlyContinue')
    print("[+] 打印服务已重启。")

# 深度重启（批量重启服务 + Explorer + DWM）
def deep_restart():
    print("[*] 正在批量重启可重启服务...")
    # 批量重启服务
    script = """
    $services = Get-Service | Where-Object { $_.Status -eq 'Running' -and $_.CanStop -eq $true }
    foreach ($svc in $services) {
        try {
            Write-Output "重启服务: $($svc.Name)"
            Restart-Service -Name $svc.Name -Force -ErrorAction SilentlyContinue
        } catch {
            Write-Output "无法重启: $($svc.Name)"
        }
    }
    """
    run_powershell(script)

    # Explorer重启
    print("[*] 正在重启 Explorer...")
    run_powershell('Stop-Process -Name explorer -Force')
    run_powershell('Start-Process explorer')

    # DWM重启
    print("[*] 正在重启 DWM（桌面窗口管理器）...")
    run_powershell('Stop-Process -Name dwm -Force')
    # 注意：dwm.exe通常由系统自动拉起，如果没有，可手动启动
    run_powershell('Start-Process dwm')

    print("[+] 深度重启已完成，祝你摆脱卡顿！")

def kill_all_svchost():
    print("==========>>>【警告】：你即将强制终止所有 svchost.exe 进程<<<==========")
    print("这可能导致系统不稳定、部分服务永久失效，甚至系统死锁。")
    confirm = input("是否继续？（输入 YES 确认）: ")
    if confirm.strip().upper() != "YES":
        print("已取消操作。")
        return

    print("[*] 正在强制终止所有 svchost.exe 进程（请保持冷静）...")
    cmd = '''
Get-Process svchost | Where-Object { $_.SessionId -ne 0 } | ForEach-Object {
    try {
        Stop-Process -Id $_.Id -Force -ErrorAction SilentlyContinue
        Write-Output "已杀: $($_.Id)"
    } catch {
        Write-Output "无法杀: $($_.Id)"
    }
}
    '''
    subprocess.run([
            "powershell.exe",
            "-NoProfile",
            "-ExecutionPolicy", "Bypass",
            "-Command", cmd
        ], check=True)
    print("[!] 操作完成，部分系统服务可能无法恢复。请视情况重启系统。")


# 菜单
def menu():
    while True:
        print("\n====== Windows 热重启工具（加强版）======")
        print('0. 检查权限')
        print("请选择要修复的组件：")
        print("1. 重启 Explorer (桌面/任务栏)")
        print("2. 重启网络服务")
        print("3. 重启音频服务")
        print("4. 重启剪贴板")
        print("5. 重启打印服务")
        print("6. 【深度重启】批量重启服务 + Explorer + DWM")
        print("7. 【危险操作】强制杀掉所有 svchost（风险极高）")
        print("8. 退出")
        choice = input("输入选项编号: ").strip()
        
        if choice == '0':
            if not is_admin():
                print('权限不足，请以管理员身份运行！')
            else:
                print('权限正常。')
        elif choice == '1':
            restart_explorer()
        elif choice == '2':
            restart_network()
        elif choice == '3':
            restart_audio()
        elif choice == '4':
            restart_clipboard()
        elif choice == '5':
            restart_print_spooler()
        elif choice == '6':
            print('==========>>>【警告】：该操作近乎完全重启图形层 + 非关键系统服务<<<==========')
            question = input('相当于把桌面环境和支撑服务全部刷新一次，风险高！\n您确定要执行吗？[Y/n]')
            if question == "Y":
                deep_restart()
        elif choice == '7':
            kill_all_svchost()
        elif choice == '8':
            print("再见！祝系统再也不抽风。")
            break
        else:
            print("无效选项，请重新输入。")

        print('\n\n')

# 主程序
if __name__ == '__main__':
    if not is_admin():
        print("请右键以【管理员身份】运行此脚本，否则部分操作将失败。")
        
        # 获取当前脚本绝对路径
        script_path = os.path.abspath(__file__)
        
        # 构造 PowerShell 命令
        cmd = f'''
    chcp 936 | Out-Null
    $pythonScript = "{script_path}"
    Start-Process python -ArgumentList "`"$pythonScript`"" -Wait -Verb RunAs
    '''
        subprocess.run([
            "powershell.exe",
            "-NoProfile",
            "-ExecutionPolicy", "Bypass",
            "-Command", cmd
        ], check=True)
        exit()

    menu()