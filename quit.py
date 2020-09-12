if window.get_active_class() == "konsole.konsole":
  keyboard.send_keys("<ctrl>+<shift>+q")
else:
  keyboard.send_keys("<ctrl>+q")