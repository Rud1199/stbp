import pyotp
totp = pyotp.TOTP("QSSWY3DPEHPK3PXP")
print("Current OTP:", totp.now())
