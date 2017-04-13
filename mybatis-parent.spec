%{?_javapackages_macros:%_javapackages_macros}

Name:          mybatis-parent
Version:       21
Release:       6%{?dist}
Summary:       The MyBatis parent POM
Group:         Development/Java
License:       ASL 2.0
URL:           http://www.mybatis.org/
Source0:       https://github.com/mybatis/parent/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)

BuildArch:     noarch

%description
The MyBatis parent POM which has to be inherited by all MyBatis modules.

%prep
%setup -q -n parent-%{name}-%{version}
# require com.github.stephenc.wagon:wagon-gitsite:0.4.1
%pom_remove_plugin org.apache.maven.plugins:maven-site-plugin
# unavailable plugins
%pom_remove_plugin org.apache.maven.plugins:maven-pdf-plugin
%pom_remove_plugin org.sonatype.plugins:jarjar-maven-plugin
%pom_remove_plugin org.sonatype.plugins:nexus-maven-plugin
%pom_remove_plugin org.codehaus.mojo:clirr-maven-plugin
%pom_remove_plugin org.codehaus.mojo:jdepend-maven-plugin
%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin
%pom_remove_plugin org.codehaus.mojo:taglist-maven-plugin

# animal-sniffer is currently broken. it uses asm4, but asm3 is loaded
%pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin

%pom_remove_plugin :maven-scm-plugin

# remove com.google.doclava:doclava:1.0.3
# javac.target.version is set 1.5
%pom_xpath_remove "pom:reporting/pom:plugins/pom:plugin[pom:artifactId ='maven-javadoc-plugin']/pom:configuration"
%pom_xpath_inject "pom:reporting/pom:plugins/pom:plugin[pom:artifactId ='maven-javadoc-plugin']" '
 <configuration>
  <minmemory>128m</minmemory>
  <maxmemory>1024m</maxmemory>
  <breakiterator>true</breakiterator>
  <quiet>true</quiet>
  <verbose>false</verbose>
  <source>${javac.target.version}</source>
  <linksource>true</linksource>
</configuration>'

%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId ='maven-enforcer-plugin']/pom:executions/pom:execution/pom:configuration/pom:rules/pom:requirePluginVersions"

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README
%doc LICENSE NOTICE

%changelog
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 21 2016 gil cattaneo <puntogil@libero.it> 21-5
- remove maven-scm-plugin

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 10 2015 gil cattaneo <puntogil@libero.it> 21-2
- introduce license macro

* Wed Dec 24 2014 gil cattaneo <puntogil@libero.it> 21-1
- update to 21

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 18-6
- Rebuild to regenerate Maven auto-requires

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 03 2013 gil cattaneo <puntogil@libero.it> 18-4
- switch to XMvn
- minor changes to adapt to current guideline

* Sat May 11 2013 gil cattaneo <puntogil@libero.it> 18-3
- disable animal-sniffer-maven-plugin

* Mon Apr 22 2013 gil cattaneo <puntogil@libero.it> 18-2
- fix requires (all active plugin listed in the pom)

* Sun Apr 21 2013 gil cattaneo <puntogil@libero.it> 18-1
- initial rpm
