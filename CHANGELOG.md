# Changelog
All notable changes to this project will be documented in this file. See [conventional commits](https://www.conventionalcommits.org/) for commit guidelines.

- - -
## [v0.7.2](https://github.com/yoctoyotta1024/microphysics_testcases/compare/110a936d9f26ff446de776f8d721c2e63dfd0996..v0.7.2) - 2025-06-04
#### Bug Fixes
- add missing total_ice calculation - ([e89ab6f](https://github.com/yoctoyotta1024/microphysics_testcases/commit/e89ab6f777f8a888c0783f6b5ae627f2cc01a759)) - Georgiana Mania
- float/double overloading problem - ([bc5db94](https://github.com/yoctoyotta1024/microphysics_testcases/commit/bc5db9456c0f4266c722da26dd4e0aeb28b5470b)) - Georgiana Mania
#### Continuous Integration
- update aritfacts - ([110a936](https://github.com/yoctoyotta1024/microphysics_testcases/commit/110a936d9f26ff446de776f8d721c2e63dfd0996)) - clara.bayley
#### Performance Improvements
- rename path to aes muphys python bindings - ([4358fc9](https://github.com/yoctoyotta1024/microphysics_testcases/commit/4358fc9a198e3a13f0db6b641b76fe8a8b50e50e)) - clara.bayley
#### Refactoring
- Update icon_graupel and icon_sat_adj based on ragnarok changes - ([a81e0ec](https://github.com/yoctoyotta1024/microphysics_testcases/commit/a81e0ecb29a505dc442f10a8ef23f2e96f4569a6)) - Georgiana Mania

- - -

## [v0.7.1](https://github.com/yoctoyotta1024/microphysics_testcases/compare/1d43cc1967216f3d5b98c05bdb01b036ff6a8be9..v0.7.1) - 2025-02-03
#### Bug Fixes
- calls after ICON MPI-M update - ([bbb4a0c](https://github.com/yoctoyotta1024/microphysics_testcases/commit/bbb4a0cc446a3f457f78d223b8db2aa562e0c63c)) - Georgiana Mania
#### Refactoring
- rename files and correct headers and docstrings - ([41050ec](https://github.com/yoctoyotta1024/microphysics_testcases/commit/41050ec74f258804660e7f8c77e985229979dc95)) - clara.bayley
- rename mock_py libs - ([bf96c10](https://github.com/yoctoyotta1024/microphysics_testcases/commit/bf96c10551033f6ecf74e8bdc07b189598c985ac)) - clara.bayley
- rename mock_cxx libs - ([522cc47](https://github.com/yoctoyotta1024/microphysics_testcases/commit/522cc47a8006a5b93fcb5eba3e2715e13f4fc93c)) - clara.bayley
- rename pympdata libs - ([d2ccad4](https://github.com/yoctoyotta1024/microphysics_testcases/commit/d2ccad4bc7650f471a0001d7932b27caef399405)) - clara.bayley
- rename graupel libs -> icon_graupel - ([1d43cc1](https://github.com/yoctoyotta1024/microphysics_testcases/commit/1d43cc1967216f3d5b98c05bdb01b036ff6a8be9)) - clara.bayley

- - -

## [v0.7.0](https://github.com/yoctoyotta1024/microphysics_testcases/compare/7ee44daeae3669de34fc9f1e2c508d9d58e48ff5..v0.7.0) - 2024-11-21
#### Bug Fixes
- run satadj tests only if PY_GRAUPEL_DIR is set - ([af23c24](https://github.com/yoctoyotta1024/microphysics_testcases/commit/af23c2474778c24acddc6a90b249c5018f0c20b1)) - clara.bayley
- missing pre-commit requirement - ([507ab94](https://github.com/yoctoyotta1024/microphysics_testcases/commit/507ab946d33092f30038a6b61f1cbce540fff414)) - clara.bayley
- ensure python version of env works for ICON python bindings - ([3f4a3b4](https://github.com/yoctoyotta1024/microphysics_testcases/commit/3f4a3b40f279f647813f4c9e2eef711b3abafa0b)) - clara.bayley
- fix pre-commit hook - ([7ee44da](https://github.com/yoctoyotta1024/microphysics_testcases/commit/7ee44daeae3669de34fc9f1e2c508d9d58e48ff5)) - clara.bayley
#### Features
- more thermodynamic variables calculated and plotted in 0d parcel - ([067b11f](https://github.com/yoctoyotta1024/microphysics_testcases/commit/067b11f2b4583e5f006fc1b401149d03e94202c9)) - clara.bayley
- tests for satadj microphysics scheme - ([7077963](https://github.com/yoctoyotta1024/microphysics_testcases/commit/7077963596da1b063b0df2f27e6dabfb9369cd2b)) - clara.bayley
- new wrapper for ICON saturation adjustment as microphysics scheme - ([3829323](https://github.com/yoctoyotta1024/microphysics_testcases/commit/382932380fe641c1023fb379a0b525ba12073744)) - clara.bayley
#### Miscellaneous Chores
- fix spelling Kg -> kg - ([e04b6aa](https://github.com/yoctoyotta1024/microphysics_testcases/commit/e04b6aa1f95d38c30b24fb033c9dbc5140662c86)) - clara.bayley
- formatting - ([2e08547](https://github.com/yoctoyotta1024/microphysics_testcases/commit/2e08547b0d3a2707f7b1800f012cccf06ac4b1df)) - clara.bayley

- - -

## [v0.6.0](https://github.com/yoctoyotta1024/microphysics_testcases/compare/150373d55e0e6ff3450fa79144dc9cf2b93006c9..v0.6.0) - 2024-11-21
#### Bug Fixes
- run graupel tests only if PY_GRAUPEL_DIR is set - ([f812bf4](https://github.com/yoctoyotta1024/microphysics_testcases/commit/f812bf4ab3e2e634522dd4a1b6bd387aaee91126)) - Georgiana Mania
- fix 1 bug - ([c59cdc1](https://github.com/yoctoyotta1024/microphysics_testcases/commit/c59cdc1ccf1c22ac24e5e859780ce895dd11b9b1)) - Georgiana Mania
#### Features
- debug info - ([f018581](https://github.com/yoctoyotta1024/microphysics_testcases/commit/f0185813938d57f7ae6baabe1662b9c95a334581)) - Georgiana Mania
- add sat adj - ([d963a02](https://github.com/yoctoyotta1024/microphysics_testcases/commit/d963a0212f9a24d63fd30ef069f006f0dfcbc3fb)) - Georgiana Mania
- first try to create pytests for ICON via python bindings - ([8fe7d3a](https://github.com/yoctoyotta1024/microphysics_testcases/commit/8fe7d3ac472ef2c2656800e23c57941a1ebe36e4)) - Georgiana Mania
#### Miscellaneous Chores
- code formatted - ([277dec2](https://github.com/yoctoyotta1024/microphysics_testcases/commit/277dec2e0d61335a4008faa4a80ea112ce6069f2)) - Georgiana Mania
- cleanup - ([a73cc98](https://github.com/yoctoyotta1024/microphysics_testcases/commit/a73cc9889d760282c7afc82611ce00e466aad6a0)) - Georgiana Mania
- rebase leftover - ([4c5f928](https://github.com/yoctoyotta1024/microphysics_testcases/commit/4c5f928696572ef157f3ad479bed9d0a29a0e5db)) - Georgiana Mania
- rebase on main - ([70ed2fe](https://github.com/yoctoyotta1024/microphysics_testcases/commit/70ed2fe389d3e1e3e526a2bcdffa2c156558f9d3)) - Georgiana Mania
#### Refactoring
- add args to conventional commits - ([5010d0a](https://github.com/yoctoyotta1024/microphysics_testcases/commit/5010d0a5cc33beadf7baea344851f80ebafb1109)) - Georgiana Mania
- add contributors - ([068bffe](https://github.com/yoctoyotta1024/microphysics_testcases/commit/068bffea0fa0cb3152244f3424d6e10303144e8b)) - Georgiana Mania
- call graupel without precip - ([dead9a4](https://github.com/yoctoyotta1024/microphysics_testcases/commit/dead9a43da4e84821d3705e962536087ab137234)) - Georgiana Mania
- rename tests - ([c6137a7](https://github.com/yoctoyotta1024/microphysics_testcases/commit/c6137a7f8075f2d2c52fe4bbdbea24d12643e5f7)) - Georgiana Mania
- mirror latest interface & bugfixes as per MPI-M master - ([a14ff82](https://github.com/yoctoyotta1024/microphysics_testcases/commit/a14ff82da52c20f224f30164dc300bc0f2bc2603)) - Georgiana Mania
- revert using mock tests; adapt plots and tests to use np.arrays - ([e72fda7](https://github.com/yoctoyotta1024/microphysics_testcases/commit/e72fda7ef50919414894316564ec9ac03f00d6c3)) - Georgiana Mania
- reverted mock files - ([2e14be4](https://github.com/yoctoyotta1024/microphysics_testcases/commit/2e14be46c8933fb9a88d1399b1d3c98561a1fd31)) - Georgiana Mania
- rename thermo to result in tests - ([150373d](https://github.com/yoctoyotta1024/microphysics_testcases/commit/150373d55e0e6ff3450fa79144dc9cf2b93006c9)) - clara.bayley

- - -

## [v0.5.1](https://github.com/yoctoyotta1024/microphysics_testcases/compare/c83d43e6564810b647ceabc501aed39b0ef628e9..v0.5.1) - 2024-11-11
#### Bug Fixes
- CI numba needs limited python version - ([3b53231](https://github.com/yoctoyotta1024/microphysics_testcases/commit/3b5323144a73becb2e24d11392190fee55fd950c)) - clara.bayley
#### Refactoring
- use arrays correctly in 0-d tests and docstrings - ([41ba03a](https://github.com/yoctoyotta1024/microphysics_testcases/commit/41ba03af18facd3c1ca56b2b4549016c6dcb83d3)) - clara.bayley
- correct label for 0dparcel microphysics tests - ([5792b85](https://github.com/yoctoyotta1024/microphysics_testcases/commit/5792b85937fcf75de4bb5137dfbc4e5923da4426)) - clara.bayley
- make dz an array and use deepcopy - ([c83d43e](https://github.com/yoctoyotta1024/microphysics_testcases/commit/c83d43e6564810b647ceabc501aed39b0ef628e9)) - clara.bayley

- - -

## [v0.5.0](https://github.com/yoctoyotta1024/microphysics_testcases/compare/9d5dc7577f7f42454fc6e650f4111581f5271d7d..v0.5.0) - 2024-09-04
#### Bug Fixes
- fix assertion - ([1d4b63b](https://github.com/yoctoyotta1024/microphysics_testcases/commit/1d4b63bb308d65dfa3291dd466e18c479597bf6f)) - clara.bayley
- use fixed output - ([7f9e8f2](https://github.com/yoctoyotta1024/microphysics_testcases/commit/7f9e8f2ddb3ab5687a47fb60af6936b4cd4bd2b9)) - clara.bayley
- fix output with arrays written to - ([9c12aa2](https://github.com/yoctoyotta1024/microphysics_testcases/commit/9c12aa2e7e27d02a142ebfa3190b526231558a72)) - clara.bayley
- minor bug fixes - ([4ca8c62](https://github.com/yoctoyotta1024/microphysics_testcases/commit/4ca8c6297ef643cb235a4afacc92c574fd5d4467)) - clara.bayley
- minor bug fixes - ([4bbb31a](https://github.com/yoctoyotta1024/microphysics_testcases/commit/4bbb31afdc325cc54905e88258cea57ba5f8c4f4)) - clara.bayley
- minor bug fixes - ([012e83b](https://github.com/yoctoyotta1024/microphysics_testcases/commit/012e83bb04024287a8ed45809571368a2da4746e)) - clara.bayley
- coarsen time for plotting - ([082c3aa](https://github.com/yoctoyotta1024/microphysics_testcases/commit/082c3aa164546045de6623f1b3bf98947afe4f69)) - clara.bayley
- correct timestepping - ([c62f28f](https://github.com/yoctoyotta1024/microphysics_testcases/commit/c62f28fd737185137af33ebddcde9fe5ae75f178)) - clara.bayley
- paths and string conversions - ([e2c95f4](https://github.com/yoctoyotta1024/microphysics_testcases/commit/e2c95f45551fa0b15c28c39ae3c3a9b9cf662f20)) - clara.bayley
- import thermodynamics - ([bdf4513](https://github.com/yoctoyotta1024/microphysics_testcases/commit/bdf4513f6a96547c31faa8f08deb61ed52d182a3)) - clara.bayley
#### Documentation
- formatting - ([c75edb9](https://github.com/yoctoyotta1024/microphysics_testcases/commit/c75edb988319ecd3d5e0d75182d47a7ed8ebb243)) - clara.bayley
- added docstrings - ([8670288](https://github.com/yoctoyotta1024/microphysics_testcases/commit/8670288f4dfac578cde073634c7b2fe010ceee6d)) - clara.bayley
- rst files for 1d kid test case - ([6ae094e](https://github.com/yoctoyotta1024/microphysics_testcases/commit/6ae094ee6abb9b20d062d2292a2a63ef0d666ab7)) - clara.bayley
- new docs for bulk microphysics scheme from KiD - ([c4572d1](https://github.com/yoctoyotta1024/microphysics_testcases/commit/c4572d1dd357b99e225b9bc023249a1af6ef0855)) - clara.bayley
- new docs for bulk microphysics scheme from KiD - ([e137033](https://github.com/yoctoyotta1024/microphysics_testcases/commit/e13703371652d6bf94a5f185ec29ca6366b441cb)) - clara.bayley
- new docs for utilities module - ([013d502](https://github.com/yoctoyotta1024/microphysics_testcases/commit/013d50273ebeda744c4a23e3d604b050e63af9d5)) - clara.bayley
- add docstrings - ([03d58f7](https://github.com/yoctoyotta1024/microphysics_testcases/commit/03d58f7f2d9de27ef783826782853915d28ef10f)) - clara.bayley
- add docstring - ([1370e2a](https://github.com/yoctoyotta1024/microphysics_testcases/commit/1370e2afbc4849641988c27e584f37feda97e714)) - clara.bayley
- update to reflect file movements - ([48b68e1](https://github.com/yoctoyotta1024/microphysics_testcases/commit/48b68e125228e6513742912ac85847934ec4ba16)) - clara.bayley
- add link to kid doc - ([d382769](https://github.com/yoctoyotta1024/microphysics_testcases/commit/d382769c21bc476a86c67796c9373dd713977d09)) - clara.bayley
- fix formatting - ([fecaf6d](https://github.com/yoctoyotta1024/microphysics_testcases/commit/fecaf6d60759231d2d0e392001969ebd72f5d9f2)) - clara.bayley
#### Features
- 0-D parcel test for bulk scheme - ([c535ae2](https://github.com/yoctoyotta1024/microphysics_testcases/commit/c535ae2e7b7b3e1bf8497ae7d6aad7632a0072ce)) - clara.bayley
- new tests for pympdata bulk scheme - ([6def8a1](https://github.com/yoctoyotta1024/microphysics_testcases/commit/6def8a1ff36d38ab93c783c67c8c277db448f33b)) - clara.bayley
- possible to output z,x and y half - ([8137f10](https://github.com/yoctoyotta1024/microphysics_testcases/commit/8137f1051a594503d147e5833825450c8cca353b)) - clara.bayley
- new file for kid dynamics - ([91b5ca6](https://github.com/yoctoyotta1024/microphysics_testcases/commit/91b5ca6053e734bc20b7de254413f6f053db55b2)) - clara.bayley
- new python file and requirements for KiD test case - ([654b057](https://github.com/yoctoyotta1024/microphysics_testcases/commit/654b05739fda01dcf050e51525faaa28106535ac)) - clara.bayley
- initial doc for new test case - ([9d5dc75](https://github.com/yoctoyotta1024/microphysics_testcases/commit/9d5dc7577f7f42454fc6e650f4111581f5271d7d)) - clara.bayley
#### Miscellaneous Chores
- format header - ([7db2dcc](https://github.com/yoctoyotta1024/microphysics_testcases/commit/7db2dcc88c843b76d21ebec503f4fabc6f3fc58a)) - clara.bayley
#### Refactoring
- file renaming - ([1410828](https://github.com/yoctoyotta1024/microphysics_testcases/commit/1410828776a3e6ca863a144776a98ae5b65e56ff)) - clara.bayley
- file rename - ([f325e96](https://github.com/yoctoyotta1024/microphysics_testcases/commit/f325e9626d191b1a4b7fa6ad23e1587615e68c32)) - clara.bayley
- file rename - ([8b125e6](https://github.com/yoctoyotta1024/microphysics_testcases/commit/8b125e63048f2324fe68ee09e65986def43b2a62)) - clara.bayley
- file rename - ([fbcfea8](https://github.com/yoctoyotta1024/microphysics_testcases/commit/fbcfea857bddccdbae0cd995ecb0506c9acc0f4c)) - clara.bayley
- file rename and more docs - ([d25becf](https://github.com/yoctoyotta1024/microphysics_testcases/commit/d25becf06564e682841b8a65c858ab225f044361)) - clara.bayley
- beautify plots - ([f523339](https://github.com/yoctoyotta1024/microphysics_testcases/commit/f52333955d4c6b1938ed0d6c0ed6e569e6ff7d14)) - clara.bayley
- modify plotting - ([29f9746](https://github.com/yoctoyotta1024/microphysics_testcases/commit/29f97465c01c01a73a37f3c7a5791078fd4a1e54)) - clara.bayley
- tidy scripts - ([d5afc87](https://github.com/yoctoyotta1024/microphysics_testcases/commit/d5afc87be0b4be28edf278f6c37a468d30b5ede5)) - clara.bayley
- work in progress plotting kid - ([ff696d5](https://github.com/yoctoyotta1024/microphysics_testcases/commit/ff696d5ecb72922deb0a56df0904a1b0121dafdf)) - clara.bayley
- improve plotting - ([6272fff](https://github.com/yoctoyotta1024/microphysics_testcases/commit/6272fffdd6b704a151f989cbf0e39140a2feee8d)) - clara.bayley
- add get item to class - ([99718a8](https://github.com/yoctoyotta1024/microphysics_testcases/commit/99718a800a3fdd62279510fe1c27b1e81f11da6a)) - clara.bayley
- move plotting function into utilities - ([1cdbe5a](https://github.com/yoctoyotta1024/microphysics_testcases/commit/1cdbe5a19bbac41c0a6fb0f39ea035141025c021)) - clara.bayley
- move useful function into seperate module - ([0a194d1](https://github.com/yoctoyotta1024/microphysics_testcases/commit/0a194d18ea11349b1806bbe90b2f8639b7df96c6)) - clara.bayley
- file rename - ([c941b25](https://github.com/yoctoyotta1024/microphysics_testcases/commit/c941b25cfbaee73a6da2ffcff8eb08c4c568160d)) - clara.bayley
- more descriptive names and docstrings - ([a820275](https://github.com/yoctoyotta1024/microphysics_testcases/commit/a820275701f0e1b2fc63be1b13223523bf65ab42)) - clara.bayley
- extrac from thermo before args for clarity - ([d8c4bc9](https://github.com/yoctoyotta1024/microphysics_testcases/commit/d8c4bc97d19fcf97b1743c18463fe4e6099bc6c0)) - clara.bayley
- seperate wrapper from microphysics scheme - ([cd25af8](https://github.com/yoctoyotta1024/microphysics_testcases/commit/cd25af872676999e71a8bdf8ab78d49ba20f3674)) - clara.bayley
- move bulk scheme to seperate file - ([40acd08](https://github.com/yoctoyotta1024/microphysics_testcases/commit/40acd08ad38a8b91ed4e482b2253d14f72630590)) - clara.bayley
- move python files - ([5b360d1](https://github.com/yoctoyotta1024/microphysics_testcases/commit/5b360d1a46303a99e4aea43e748db4bf24f50572)) - clara.bayley
- create bulk microphysics scheme - ([3314253](https://github.com/yoctoyotta1024/microphysics_testcases/commit/33142536ee6d3f5c09c8e56edf63f226c16c37f6)) - clara.bayley
- create bulk microphysics scheme - ([5b613a0](https://github.com/yoctoyotta1024/microphysics_testcases/commit/5b613a0ea1440889531c8aec74964489fa00d7fa)) - clara.bayley
- create bulk microphysics scheme - ([d63d629](https://github.com/yoctoyotta1024/microphysics_testcases/commit/d63d629f9d6f8696e240be791a0fdc7334319f1e)) - clara.bayley
- kid influences thermo for output - ([67844f7](https://github.com/yoctoyotta1024/microphysics_testcases/commit/67844f7eaa346befdaacec0c127cff229f36d66b)) - clara.bayley
- better imports - ([9e77680](https://github.com/yoctoyotta1024/microphysics_testcases/commit/9e776807dfc2e241d1568ac0ad708b4cf4a78d06)) - clara.bayley
- rename test - ([fc2ee43](https://github.com/yoctoyotta1024/microphysics_testcases/commit/fc2ee43cf2179f02d703692f2a99ca48b1a2728d)) - clara.bayley
- turn kid into test for pytest - ([81045a9](https://github.com/yoctoyotta1024/microphysics_testcases/commit/81045a915026c063c429c6c4a29788c038fa01b7)) - clara.bayley
- use kid dynamics in run_kid1d - ([005d85c](https://github.com/yoctoyotta1024/microphysics_testcases/commit/005d85cd3cd2b153bbebb5a61a648717128ce4fc)) - clara.bayley
- move kid into run function - ([18ba831](https://github.com/yoctoyotta1024/microphysics_testcases/commit/18ba8318b466dfe72bc5b2f5dd664afb6db48d1a)) - clara.bayley
- rename and change init args - ([4a93991](https://github.com/yoctoyotta1024/microphysics_testcases/commit/4a93991211dfe9a7daf54120703cc10e49528223)) - clara.bayley
- move prof into kid dynamics class - ([8dabc2f](https://github.com/yoctoyotta1024/microphysics_testcases/commit/8dabc2fecbd7aa6fa93cbb447fac0ef2d736ac02)) - clara.bayley
- move init of kid into class - ([2c39323](https://github.com/yoctoyotta1024/microphysics_testcases/commit/2c39323fb11f071eabfda51fdcbeb048a0605301)) - clara.bayley
- remove adaptive dt - ([a0f20c8](https://github.com/yoctoyotta1024/microphysics_testcases/commit/a0f20c8f6ea53b088113ab2dd803be372d4bee19)) - clara.bayley
- new files for organising test case - ([f496a58](https://github.com/yoctoyotta1024/microphysics_testcases/commit/f496a588ff4a7febd3b792ede06fd81234e4d47c)) - clara.bayley
- add file descriptions - ([133e03f](https://github.com/yoctoyotta1024/microphysics_testcases/commit/133e03f2ae16cc795c761f87bb1cdd35472b97cd)) - clara.bayley
- file renamings - ([5a05ee8](https://github.com/yoctoyotta1024/microphysics_testcases/commit/5a05ee88dc101b0e44e80cd100000f0fa270d162)) - clara.bayley
- KiD working with default bulk scheme - ([46ff18d](https://github.com/yoctoyotta1024/microphysics_testcases/commit/46ff18d9ea59a25a26214634c0ee9b61795e4c1e)) - clara.bayley
- improve use of path - ([4b9bf73](https://github.com/yoctoyotta1024/microphysics_testcases/commit/4b9bf7336c02a1df5fce5b0461f92faba71a31ac)) - clara.bayley
- add numba requirement - ([deaf09e](https://github.com/yoctoyotta1024/microphysics_testcases/commit/deaf09e00d7951cf8bbcf246d038ee2d9067dcfe)) - clara.bayley
- working to add kid test case - ([c081c13](https://github.com/yoctoyotta1024/microphysics_testcases/commit/c081c13fa82fe701984d572a1385d0bd00ba53ad)) - clara.bayley

- - -

## [v0.4.2](https://github.com/yoctoyotta1024/microphysics_testcases/compare/34b17e37a911a0e9d4ed9ec2a1dbfe95ec2c73e2..v0.4.2) - 2024-09-04
#### Bug Fixes
- Security vulnerability - ([dcb9243](https://github.com/yoctoyotta1024/microphysics_testcases/commit/dcb92433c1386b52656b66dc5ac09aa5982c7870)) - clara.bayley
#### Documentation
- refer to working example in docs - ([c831a0a](https://github.com/yoctoyotta1024/microphysics_testcases/commit/c831a0a25ea49bd540dfdde247518b31eacc20c7)) - clara.bayley
- more info for context - ([4e3b67f](https://github.com/yoctoyotta1024/microphysics_testcases/commit/4e3b67f584d4e89acb2c5568edf9fc56a19ec648)) - clara.bayley
#### Refactoring
- rename files - ([4c02f65](https://github.com/yoctoyotta1024/microphysics_testcases/commit/4c02f6523a283ef77e239c3d109e53083e780dfc)) - clara.bayley
- rename mock modules for clarity - ([34b17e3](https://github.com/yoctoyotta1024/microphysics_testcases/commit/34b17e37a911a0e9d4ed9ec2a1dbfe95ec2c73e2)) - clara.bayley

- - -

## [v0.4.1](https://github.com/yoctoyotta1024/microphysics_testcases/compare/f30018fb88007d96f83c96c5cf903653689406a2..v0.4.1) - 2024-09-01
#### Bug Fixes
- fix sphinx latest version issues with deprecated utils functions removed - ([f70d9a4](https://github.com/yoctoyotta1024/microphysics_testcases/commit/f70d9a4da5dfa60a0ee9fd0036d1063ccc0ff19e)) - clara.bayley
- limit sphinx version due to bug - ([ad2d9d5](https://github.com/yoctoyotta1024/microphysics_testcases/commit/ad2d9d5c99e1e90462a82df398ed064815866e1e)) - clara.bayley
#### Miscellaneous Chores
- formatting - ([b76cd96](https://github.com/yoctoyotta1024/microphysics_testcases/commit/b76cd9681ed900b4687fe87f4e3aa36e57100135)) - clara.bayley
#### Refactoring
- rename .yml -> .yaml - ([b583c7c](https://github.com/yoctoyotta1024/microphysics_testcases/commit/b583c7cc3bb962865b848dab563890e8c9094423)) - clara.bayley
- rename env in yaml - ([c542e3f](https://github.com/yoctoyotta1024/microphysics_testcases/commit/c542e3fc0d3d303051d42035a3a8bf7fa3b12ece)) - clara.bayley
- add more precommit hooks and descriptions - ([f30018f](https://github.com/yoctoyotta1024/microphysics_testcases/commit/f30018fb88007d96f83c96c5cf903653689406a2)) - clara.bayley

- - -

## [v0.4.0](https://github.com/yoctoyotta1024/microphysics_testcases/compare/8411a87f9b4849e7b833a31ec0e5b6e7067057cd..v0.4.0) - 2024-06-17
#### Features
- added more pre-commit hooks - ([8411a87](https://github.com/yoctoyotta1024/microphysics_testcases/commit/8411a87f9b4849e7b833a31ec0e5b6e7067057cd)) - clara.bayley
#### Miscellaneous Chores
- note in file (to force version bump) - ([f02f385](https://github.com/yoctoyotta1024/microphysics_testcases/commit/f02f385f7e02422574c5e1f4703492996194156c)) - clara.bayley
- formatting python files with ruff linter and formatter - ([c4ddab9](https://github.com/yoctoyotta1024/microphysics_testcases/commit/c4ddab92e5b66eea576b709f9884fb72e68701e6)) - clara.bayley

- - -

## [v0.3.0](https://github.com/yoctoyotta1024/microphysics_testcases/compare/1d42a15e3026bf458db4a76d6ac3d155c8e1bbec..v0.3.0) - 2024-06-17
#### Features
- Thermodynamics uses np.arrays not floats for variables - ([7aea676](https://github.com/yoctoyotta1024/microphysics_testcases/commit/7aea676567a276125a6ce010dce1f23633c008b2)) - clara.bayley
- Thermodynamics uses np.arrays not floats for variables - ([8d62ef7](https://github.com/yoctoyotta1024/microphysics_testcases/commit/8d62ef7694c485833b31bd4b085a912b43fb5b00)) - clara.bayley
#### Refactoring
- make scripts and tests compatible with thermodyanmics as arrays - ([eafcc99](https://github.com/yoctoyotta1024/microphysics_testcases/commit/eafcc991d73f32e1900315378ae2576086e8ad67)) - clara.bayley
- require reference pressure explictly for theta calc - ([1d42a15](https://github.com/yoctoyotta1024/microphysics_testcases/commit/1d42a15e3026bf458db4a76d6ac3d155c8e1bbec)) - clara.bayley

- - -

## [v0.2.5](https://github.com/yoctoyotta1024/microphysics_testcases/compare/3d692d91d6215c455d1a5a7dcd04a7d3139ad285..v0.2.5) - 2024-05-02
#### Bug Fixes
- restore changelog - ([e45f803](https://github.com/yoctoyotta1024/microphysics_testcases/commit/e45f8036669f701d9d2c663da473ab110c9b8602)) - clara.bayley
- minor changes to pre and post bump echos - ([3d692d9](https://github.com/yoctoyotta1024/microphysics_testcases/commit/3d692d91d6215c455d1a5a7dcd04a7d3139ad285)) - clara.bayley

- - -

## [v0.2.4](https://github.com/yoctoyotta1024/microphysics_testcases/compare/v0.2.3..v0.2.4) - 2024-05-02
#### Bug Fixes
- add git push post bump to try to update logs - ([a150c44](https://github.com/yoctoyotta1024/microphysics_testcases/commit/a150c44cae41ec87062d690258bd70e7c9feb45d)) - clara.bayley
#### Miscellaneous Chores
- **(version)** v0.2.4 - ([fa59b1e](https://github.com/yoctoyotta1024/microphysics_testcases/commit/fa59b1e2e648332375a40ff0eb0ed6c312da9b79)) - yoctoyotta1024

- - -

## [v0.2.3](https://github.com/yoctoyotta1024/microphysics_testcases/compare/v0.2.2..v0.2.3) - 2024-05-02
#### Bug Fixes
- delete unwanted print statements at end of workflow - ([ee965a1](https://github.com/yoctoyotta1024/microphysics_testcases/commit/ee965a12574d501a30172d7976d0dbd14289c81a)) - clara.bayley
#### Refactoring
- test what's in changelog - ([6c2234c](https://github.com/yoctoyotta1024/microphysics_testcases/commit/6c2234c983caf3c0535cb4fac0d95f728c166aaf)) - clara.bayley

- - -

## [v0.2.2](https://github.com/yoctoyotta1024/microphysics_testcases/compare/v0.2.1..v0.2.2) - 2024-05-02
#### Bug Fixes
- change to changelog styling - ([9e152f6](https://github.com/yoctoyotta1024/microphysics_testcases/commit/9e152f6bacfc40b11e3682cc57ea397b42e14719)) - clara.bayley

- - -

## [v0.2.1](https://github.com/yoctoyotta1024/microphysics_testcases/compare/v0.2.0..v0.2.1) - 2024-05-02
#### Bug Fixes
- release on github - ([6546aab](https://github.com/yoctoyotta1024/microphysics_testcases/commit/6546aabce59a0995d19ba84cb823f6aa56470b5c)) - clara.bayley

- - -

## [v0.2.0](https://github.com/yoctoyotta1024/microphysics_testcases/compare/v0.1.1..v0.2.0) - 2024-05-02
#### Bug Fixes
- delete post bump hooks that fail when merging to main on github - ([e56d6ca](https://github.com/yoctoyotta1024/microphysics_testcases/commit/e56d6cafc2f99f7c8448461afd0a630213970b9a)) - clara.bayley
- bug fixes to fetch repo commmits in release with cocogitto - ([75232aa](https://github.com/yoctoyotta1024/microphysics_testcases/commit/75232aa03b0532f22f027249919ef1a1ab4b27de)) - clara.bayley
- bug fixes to fetch repo commmits in release with cocogitto - ([0a79d9a](https://github.com/yoctoyotta1024/microphysics_testcases/commit/0a79d9a09da85335ccbcbd338e5683635012fc68)) - clara.bayley
- remove bad versioning in cmake - ([33c5443](https://github.com/yoctoyotta1024/microphysics_testcases/commit/33c544334267406721924955c5d111cc88d30283)) - clara.bayley
#### Features
- automatic versioning in cocogitto CI - ([37dc929](https://github.com/yoctoyotta1024/microphysics_testcases/commit/37dc9297a654e680997f63b5007d281c3c66ed25)) - clara.bayley
- cocogitto ci occurs on pushes - ([bc7b5f1](https://github.com/yoctoyotta1024/microphysics_testcases/commit/bc7b5f1d4b7f26f52e582bd25b3696e989d37b89)) - clara.bayley
- new workflow in CI for cocogitto - ([88b9b24](https://github.com/yoctoyotta1024/microphysics_testcases/commit/88b9b240173cccf4454e9f767f7cfb5d0a1a8fe3)) - clara.bayley
#### Miscellaneous Chores
- **(version)** v0.2.0 - ([706e280](https://github.com/yoctoyotta1024/microphysics_testcases/commit/706e280b7191cfcb6765ae294cbf295b0d82980e)) - clara.bayley
- **(version)** v0.1.0 - ([0f110d6](https://github.com/yoctoyotta1024/microphysics_testcases/commit/0f110d6144c5db762b7781179145cdcd0d871117)) - yoctoyotta1024
- **(version)** v0.1.0 - ([aa0c4cb](https://github.com/yoctoyotta1024/microphysics_testcases/commit/aa0c4cb063166332da8226b91a1ca213442711f6)) - yoctoyotta1024
- whitespace - ([e837b9e](https://github.com/yoctoyotta1024/microphysics_testcases/commit/e837b9e352fd30c1efd548c6e4a99f7745d7c53b)) - clara.bayley

- - -

## [v0.1.1](https://github.com/yoctoyotta1024/microphysics_testcases/compare/2dab34dee899f70785c24ce97b45f3e5979a12d0..v0.1.1) - 2024-05-02
#### Bug Fixes
- manual versioning given X.Y.Z - ([3b38fac](https://github.com/yoctoyotta1024/microphysics_testcases/commit/3b38fac0c91b29a66fe2156ee9ade4a924681316)) - clara.bayley
#### Miscellaneous Chores
- **(version)** v0.1.1 - ([73320c8](https://github.com/yoctoyotta1024/microphysics_testcases/commit/73320c822ad265eed75bfb4a2ec120daf268e445)) - clara.bayley
- whitespace - ([2dab34d](https://github.com/yoctoyotta1024/microphysics_testcases/commit/2dab34dee899f70785c24ce97b45f3e5979a12d0)) - clara.bayley

- - -

This changelog was generated by [cocogitto](https://github.com/oknozor/cocogitto).
