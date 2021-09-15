import re

pattern = re.compile("public static final License EMPTY_LICENSE[\s\S]+(?=};)};\n")

f = open("core/src/main/java/ch/cyberduck/core/aquaticprime/LicenseFactory.java","r+",encoding="utf8")
licensefactory=f.read()

EMPTY_LICENSE = pattern.findall(licensefactory)[0]

PATCHED_LICENSE = """

    public static final License PATCHED_LICENSE = new License() {
        @Override
        public boolean verify(final LicenseVerifierCallback callback) {
            return true;
        }

        @Override
        public String getValue(String property) {
            return "self-licensed";
        }

        @Override
        public String getName() {
            return LocaleFactory.localizedString("self-licensed", "License");
        }

        @Override
        public boolean isReceipt() {
            return true;
        }

        @Override
        public boolean equals(Object obj) {
            if(obj instanceof License) {
                return PATCHED_LICENSE == obj;
            }
            return false;
        }

        @Override
        public int hashCode() {
            return this.toString().hashCode();
        }

        @Override
        public String toString() {
            return LocaleFactory.localizedString("self-licensed", "License");
        }
    };

    """
patched = licensefactory.replace(EMPTY_LICENSE,EMPTY_LICENSE+PATCHED_LICENSE).replace("LicenseFactory.EMPTY_LICENSE","LicenseFactory.PATCHED_LICENSE")
f.seek(0)
f.write(patched)
f.close()