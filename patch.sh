orig=$(cat LicenseFactory.java  | tr "\n" "\r" | grep -Pzo "public static final License EMPTY_LICENSE = new License\(\) \{[\s\S]+(?=};)};")
rep=$(echo $orig | sed s/'return false'/'return true'/g | sed s/'return null'/'return \"1\"'/g | sed s/'LocaleFactory.localizedString("Not a valid registration key", "License")'/\"patched\"/g | sed s/EMPTY_LICENSE/PATCHED_LICENSE/g)
cat LicenseFactory.java | tr "\n" "\r" | sed "s/$orig/$orig\n$rep/g" | sed "s/LicenseFactory.EMPTY_LICENSE/LicenseFactory.PATCHED_LICENSE/g" | tr "\r" "\n" > LicenseFactory.java
echo patched
